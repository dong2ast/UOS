import pandas as pd

result = []

def alcohol():
    df = pd.read_csv('./csv/whisky.csv')
    name = df["name"].values.tolist()
    alcohol = df["alcohol"].values.tolist()
    for i in range(len(alcohol)):
        print(i)
        alcohol[i] = float(alcohol[i][:-1])

    for i in alcohol:
        temp = []
        for j in alcohol:
            temp.append(round(abs(i-j) ** 2, 1))
        result.append(temp)

    frame = pd.DataFrame(result, columns=name, index=name)
    frame.to_csv("alcohol.csv", encoding='utf-8-sig')
