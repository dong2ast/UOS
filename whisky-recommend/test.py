import pandas as pd
import numpy as np

MAX = 6654

df = pd.read_csv('./csv/cf_result.csv')

testdata = list(map(int,input().split()))

arr = df.to_numpy()

rank = [[0,i]for i in range(MAX)]
#
for j in testdata[:3]:
    for i in range(6654):
        rank[i][0] += arr[i,j]
rank.sort(reverse=True)

print(rank[:5])
print(rank[-6:-1])
for i in range(MAX):
    if testdata[3] == rank[i][1]:
        print(f"{testdata[3]} ranked {i+1}")
    if testdata[4] == rank[i][1]:
        print(f"{testdata[4]} ranked {i+1}")

print(arr[6100,5521])