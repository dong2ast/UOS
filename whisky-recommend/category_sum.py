import pandas as pd


def category_sum():
    df = pd.read_csv('./csv/whisky.csv')

    df['category'].replace(
        ["Belgian Whisky", "Bhutanese Whisky", "Corn Whiskey", "Danish", "Dutch", "English Whisky", "German Whisky",
         "Icelandic Whisky and Malt Spirit", "Italian", "Liechtenstein", "Light Whiskey", "Multinational Whisky",
         "New Zealand", "Poitín", "Polish Whisky", "Romanian", "Spanish Whisky", "South African Whisky", "Swiss",
         "Taiwanese Whisky", "Unspecified Single Malt", "Welsh Whisky", "Wheat Whiskey", "White Whiskey",
         "World Whisky"], "ETC", inplace=True)
    df['category'].replace("American Malt Whiskey", "American Whiskey", inplace=True)
    df['category'].replace("Austrian Whisky", "Australian Whisky", inplace=True)
    df['category'].replace(
        ["Blended American Whiskey", "Blended Belgian Whisky", "Blended French Whisky", "Blended Grain Scotch Whisky",
         "Blended Irish Whiskey", "Blended Japanese Whisky", "Blended Malt Scotch Whisky", "Blended Scotch Whisky",
         "English Blended Whisky"], "Blended Whisky", inplace=True)
    df['category'].replace("Irish Single Pot Still", "Irish Single Malt", inplace=True)
    df['category'].replace(["Japanese Single Malt", "Japanese Rice Whisky"], "Japanese Whisky", inplace=True)
    df['category'].replace(["English Grain Whisky & Spirit", "Japanese Single Grain", "Single Grain Irish Whiskey",
                            "Single Grain Belgian Whisky"], "Grain Whisky", inplace=True)
    df['category'].replace(["Single Malt Belgian Whisky", "Single Malt English Whisky", "Single Malt Finnish Whisky",
                            "Single Malt French Whisky", "Single Malt Indian Whisky", "Single Malt Swedish Whisky"],
                           "Single Malt Whisky", inplace=True)


    df.to_csv("./csv/whisky_category_sum.csv", encoding='utf-8-sig')
