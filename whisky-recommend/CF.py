import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def cf():
    dense = pd.read_csv("./csv/test.csv", index_col="index")
    t = dense.T
    similarity_rate = cosine_similarity(t)
    similarity_rate_df = pd.DataFrame(data=similarity_rate, index=t.index, columns=t.index)
    similarity_rate_df.to_csv("./csv/cf_result.csv", encoding='utf-8-sig')