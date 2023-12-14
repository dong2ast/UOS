import pandas as pd
import numpy as np

MAX = 6654

df = pd.read_csv('./csv/cf_result.csv', index_col="index")
td = pd.read_csv('./csv/test_data.csv').T

arr = df.to_numpy()
ar2 = td.to_numpy()

result = 0

for k in ar2:
    rank = [[0, i] for i in range(MAX)]
    temp = 0

    for j in k[:3]:
        for i in range(6654):
            rank[i][0] += arr[i, j]
    rank.sort(reverse=True)

    print("-----------------------base insert-----------------------")

    for j in range(MAX):
        if rank[j][1] == k[3] or rank[j][1] == k[4]:
            print(j)
            temp += j
    print(temp/2)
    result += temp/2

result /= len(ar2)

print(result)


