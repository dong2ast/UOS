import pandas as pd


def dense():
    ud = pd.read_csv("./csv/user data/index_user_whisky.csv")
    cos = pd.read_csv("./csv/cosine_sim.csv")
    cos.set_index('index', inplace=True)

    result = initial_setting(cos, ud)

    make_dense(cos, result, ud)

    result.to_csv("./csv/test.csv", encoding='utf-8-sig')


def initial_setting(cos, ud):
    col = ud.iloc[:, 1]
    df_concat = cos[str(col[0])].copy()
    df_concat.name = 1

    for i in range(1, 5):
        df_concat += cos[str(col[i])]

    df_concat /= 5

    for n in col:
        df_concat.loc[n] = 1.

    result = df_concat.to_frame().T

    return result


def make_dense(cos, result, ud):
    for i in range(2, len(ud.columns)):
        col = ud.iloc[:, i]  # 1명의 유저
        df_concat = cos[str(col[0])].copy()  # 1 위스키에 대한 상대적 유사도
        df_concat.name = i

        size = 5

        for j in range(1, 5):
            # if pd.isna(col[j]):
            if col[j] == 99999:
                size = 4
                break
            df_concat += cos[str(col[j])]  # 5 위스키의 상대적 유사도의 합

        df_concat /= size  # 5로 나눔

        for n in col:
            df_concat[n] = 1.0

        result.loc[i] = df_concat  # result dataframe에 추가

        print(i)
