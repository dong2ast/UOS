import numpy as np
import pandas as pd

MAX = 6654

df = pd.read_csv('./predicted_ratings.csv', index_col="user_id")
td = pd.read_csv('./csv/test_data.csv').T

result = 0

for i in range(len(td)):
    t = pd.Series.sort_values(df.iloc[i], ascending=False).index.to_numpy()
    temp = 0

    for k in td.iloc[i, :][3:5]:
        temp += np.where(t == str(k))[0][0]

    result += temp / 2

result /= len(td)

print("평균 Rank = " + str(result))
