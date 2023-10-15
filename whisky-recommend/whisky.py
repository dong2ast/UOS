import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def change_data(season, year):
    driver.get(
        "https://whiskyadvocate.com/ratings-reviews?custom_rating_issue%5B0%5D=" + season + "+" + year)
    time.sleep(2)
    driver.implicitly_wait(2)


def getItemContent():
    temp = driver.find_element(By.XPATH,
                               '//*[@id="directoryResults"]')
    driver.implicitly_wait(10)  # selenium에서 가끔씩 태그 시간내에 못찾는 경우 때문에 일부러 길게 설정해놓음
    return temp.find_elements(By.CSS_SELECTOR, 'div > div > a')


def crawling(season, year, name, alcohol, score, category, price, links):
    change_data(season, year)
    target = getItemContent()

    for t in target:
        temp = t.find_element(By.CSS_SELECTOR, 'div > h5').text
        if ',' in temp:
            temp = temp.split(',')
            name.append(','.join(temp[:-1]))
            alcohol.append(temp[-1].strip())
        else:
            name.append(temp)
            alcohol.append("")

        score.append(t.find_element(By.CSS_SELECTOR, 'div > div > h2').text)
        tag = t.find_element(By.CSS_SELECTOR, ' div > div > div > h6').text.split('\n')
        if len(tag) != 1:
            category.append(tag[0])
            price.append(tag[1])
        else:
            category.append('')
            price.append(tag[0])
        links.append(t.get_attribute('href'))


def whisky():
    season = ['Spring', 'Summer', 'Fall', 'Winter']

    name = []
    alcohol = []
    score = []
    category = []
    price = []
    links = []
    description = []

    crawling('Spring', '1992', name, alcohol, score, category, price, links)

    for s in season:
        for y in range(2000, 2024, 1):
            crawling(str(s), str(y), name, alcohol, score, category, price, links)

    df = pd.DataFrame(name, columns=['name'])
    df['alcohol'] = alcohol
    df['score'] = score
    df['category'] = category
    df['price'] = price
    df['links'] = links
    df.to_csv("whisky.csv", index=False, encoding='utf-8-sig')
