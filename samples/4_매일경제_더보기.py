from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd

driver = webdriver.Chrome()

# 매일뉴스 경제면
URL = "https://www.mk.co.kr/news/economy/"

driver.get(URL)

# 페이지 로딩 기다리기
time.sleep(2)

button = driver.find_element(
    value="#container > section > div.mk_body_news_group > div > div > div.col.main_col > section.news_sec.latest_news_sec > div > div > div > button",
    by=By.CSS_SELECTOR,
)

for i in range(5):
    # 버튼이 있는 위치로 이동하기
    ActionChains(driver).move_to_element(button).perform()
    button.click()
    # 로딩 기다리기
    time.sleep(1)

list = driver.find_elements(value="#list_area > li", by=By.CSS_SELECTOR)

title_list = []
body_list = []
src_list = []

for item in list:
    try:
        title = item.find_element(
            value="a > div.txt_area > h3", by=By.CSS_SELECTOR
        ).text
        body = item.find_element(value="a > div.txt_area > p", by=By.CSS_SELECTOR).text
        src = item.find_element(value="img", by=By.CSS_SELECTOR).get_attribute("src")
        title_list.append(title)
        body_list.append(body)
        src_list.append(src)
    except:
        continue

df = pd.DataFrame({"제목": title_list, "본문": body_list, "썸네일": src_list})

df.to_csv("매일경제.csv")
