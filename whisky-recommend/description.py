import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def change_view(link):
    driver.get(link)
    time.sleep(1)
    driver.implicitly_wait(1)


def get_discription(links, description):  # 설명 가져오기
    count = 1
    for l in links:
        change_view(l)
        print(count)
        count += 1
        try:
            temp = driver.find_element(By.CSS_SELECTOR,
                                       '.mwPageArea > div > div > article > div > section > div > div > div.row > div.col-lg-8 > div.postDetailsContent')
            driver.implicitly_wait(10)  # selenium에서 가끔씩 태그 시간내에 못찾는 경우 때문에 일부러 길게 설정해놓음
            description.append(temp.get_attribute('innerText'))
        except NoSuchElementException:
            description.append(" ")


def description():
    df = pd.read_csv('whisky.csv')

    description = []

    get_discription(df['links'], description)
    df['description'] = description
    df['description'] = df['description'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)  # 특수 문자 제거

    df.to_csv("result.csv", index=False)
