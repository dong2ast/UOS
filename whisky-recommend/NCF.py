import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Model
from keras.layers import Input, Embedding, Flatten, Concatenate, Dense



# CSV 파일 로드
data = pd.read_csv('./csv/test.csv')

# 사용자 및 아이템 수 계산
num_users = data['user_id'].nunique()
num_items = len(data.columns) - 1  # item 열의 개수

# 사용자 및 아이템 ID를 정수로 인코딩
user_mapping = {user_id: idx for idx, user_id in enumerate(data['user_id'].unique())}
data['user'] = data['user_id'].map(user_mapping)

# 훈련 및 테스트 데이터로 분할
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# 훈련 및 테스트 데이터셋 생성
train_user_input = train_data['user'].values
train_item_input = train_data.drop(['user_id', 'user'], axis=1).values
train_labels = train_item_input.reshape((len(train_item_input), num_items))  # 레이블 데이터 크기 조정

test_user_input = test_data['user'].values
test_item_input = test_data.drop(['user_id', 'user'], axis=1).values
test_labels = test_item_input.reshape((len(test_item_input), num_items))  # 레이블 데이터 크기 조정

# NCF 모델 정의
embedding_dim = 50

user_input = Input(shape=(1,), dtype='int32', name='user_input')
item_input = Input(shape=(num_items,), dtype='float32', name='item_input')

user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim, input_length=1)(user_input)
item_embedding = Embedding(input_dim=num_items, output_dim=embedding_dim, input_length=num_items)(item_input)

user_flatten = Flatten()(user_embedding)
item_flatten = Flatten()(item_embedding)
concat = Concatenate()([user_flatten, item_flatten])

fc1 = Dense(64, activation='relu')(concat)
fc2 = Dense(32, activation='relu')(fc1)
output = Dense(num_items, activation='sigmoid')(fc2)  # 출력 뉴런의 수를 아이템의 개수로 변경

model = Model(inputs=[user_input, item_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 훈련
model.fit([train_user_input, train_item_input], train_labels, epochs=30, batch_size=64,
          validation_data=([test_user_input, test_item_input], test_labels))

model.save("ncf_model.keras")
