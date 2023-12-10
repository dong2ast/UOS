import numpy as np
import pandas as pd
from keras.models import load_model

# 모델 불러오기
loaded_model = load_model("ncf_model.keras")

# CSV 파일 경로
csv_file_path = './csv/test_NCF.csv'  # 실제 파일 경로로 수정

# CSV 파일 로드
data = pd.read_csv(csv_file_path)

# 사용자 ID에 대한 예측을 수행하고 결과를 새로운 열에 추가
predicted_ratings = []

user_mapping = {user_id: idx for idx, user_id in enumerate(data['user_id'].unique())}

for user_id_to_predict in data['user_id'].unique():
    # 불러온 모델의 입력 형태와 동일하게 사용자 ID를 변환
    user_input_to_predict = np.array([user_mapping[user_id_to_predict]])

    # CSV 파일에서 해당 사용자에 대한 아이템 정보 가져오기
    item_info_to_predict_multiple = data[data['user_id'] == user_id_to_predict].iloc[:, 1:].values

    # 불러온 모델을 사용하여 예측
    predictions_multiple = loaded_model.predict([user_input_to_predict, item_info_to_predict_multiple])

    # 평균 예측값을 계산하여 결과 리스트에 추가
    average_prediction = np.mean(predictions_multiple.flatten())
    predicted_ratings.append(average_prediction)

# 예측값을 CSV 파일에 추가
data['predicted_rating'] = predicted_ratings

# 예측 결과를 새로운 CSV 파일로 저장
data.to_csv('predicted_ratings.csv', index=False)
