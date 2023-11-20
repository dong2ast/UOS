import pandas as pd


def dense():
    ud = pd.read_csv("./csv/user data/user_whisky.csv")
    cos = pd.read_csv("./csv/cos_sim_by_name.csv")
    cos.set_index('name', inplace=True)

    result = initial_setting(cos, ud)

    # make_dense(cos, result, ud)

    result.to_csv("./csv/test.csv", encoding='utf-8-sig')


def initial_setting(cos, ud):
    col = ud.iloc[:, 1]
    df_concat = cos[col[0]]
    for i in range(1, 5):
        df_concat += cos[col[i]]
    df_concat /= 5
    result = df_concat.to_frame().T
    return result


def make_dense(cos, result, ud):
    for i in range(2, len(ud.columns)):
        col = ud.iloc[:, i]  # 1명의 유저
        df_concat = cos[col[0]]  # 1 위스키에 대한 상대적 유사도

        size = 5

        for j in range(1, 5):
            if pd.isna(col[j]):
                size = 4
                break
            df_concat += cos[col[j]]  # 5 위스키의 상대적 유사도의 합

        df_concat /= size  # 5로 나눔
        result._append(df_concat, ignore_index=True)  # result dataframe에 추가

        print(i)