import pandas as pd


def set_solution():
    df = pd.read_csv('whisky_category.csv')

    userlog = df.iloc[0].to_list()[1:]
    userlog += df.iloc[3].to_list()[1:]
    userlog += df.iloc[6].to_list()[1:]
    userlog += df.iloc[9].to_list()[1:]
    userlog += df.iloc[12].to_list()[1:]
    puredata = df.iloc[1].to_list()[1:]
    puredata += df.iloc[4].to_list()[1:]
    puredata += df.iloc[7].to_list()[1:]
    puredata += df.iloc[10].to_list()[1:]
    puredata += df.iloc[13].to_list()[1:]

    gift = {}

    diff = [u == p for u, p in zip(userlog, puredata)]

    for i in range(len(diff)):
        # 두 값이 일치하지 않을 때
        if not diff[i]:
            # 이미 입력된 위스키라면
            if puredata[i] in gift:
                # 동일 case가 입력되지 않았다면
                if userlog[i] not in gift[puredata[i]]:
                    # 위스키 데이터에 userlog case
                    gift[puredata[i]].append(userlog[i])
            else:
                gift[puredata[i]] = [userlog[i]]

    new_df = pd.DataFrame.from_dict(gift, orient='index')
    new_df = new_df.transpose()
    new_df.to_csv("name_exception.csv", index=False, encoding='utf-8-sig')
