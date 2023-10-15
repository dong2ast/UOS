import pandas as pd

list = ["Single Malt Scotch", "American Whiskey", "Rye Whiskey", "Japanese Whisky", "Bourbon/Tennessee", "Irish", "Blended Irish Whiskey", "Blended Scotch Whisky", "Canadian", "Irish Single Pot Still", "Welsh Whisky", "Single Malt American Whiskey"]
result = []

def category():
    df = pd.read_csv('./csv/user_category.csv')
    # 위스키 advocate 카테고리
    for ct in list:
        s = []

        for column in df:
            # user log 카테고리 csv의 column마다 list 가져오기
            temp = df[column].values.tolist()
            # list 안에 카테고리가 있을 때
            if ct in temp:
                for i in range(5):
                    #각 요소마다 카테고리인지 비교
                    if temp[i] == ct:
                        # 카테고리를 제외한 항목 s에 추가 (중복 참조 가능)
                        for j in range(5):
                            if i == j:
                                continue
                            s.append(temp[j])
        count = []
        # 위스키 advocate 카테고리
        for x in list:
            count.append(s.count(x))
        result.append(count)
    frame = pd.DataFrame(result, columns=list, index=list)
    frame.to_csv("./csv/relation2.csv", encoding='utf-8-sig')
