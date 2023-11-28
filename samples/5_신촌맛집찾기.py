from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import pyautogui

search = pyautogui.prompt('검색어 입력하기')

driver = webdriver.Chrome()

URL = 'https://map.naver.com'

driver.get(URL)

# 초기 로딩
time.sleep(2)

input = driver.find_element(by=By.CSS_SELECTOR, value='.input_search') # id사용시 에러 발생

input.send_keys(search)
input.send_keys(Keys.ENTER)

# 검색 결과 로드
time.sleep(2)

driver.switch_to.frame(driver.find_element(by=By.CSS_SELECTOR, value='#searchIframe')) # frame 전환

title_arr = []

#  page까지
for _ in range(3):
    while True:
        scroll_height = driver.execute_script('return document.querySelector("#_pcmap_list_scroll_container").scrollHeight')

        driver.execute_script('document.querySelector("#_pcmap_list_scroll_container").scrollBy(0, document.querySelector("#_pcmap_list_scroll_container").scrollHeight)')

        # 신규 데이터 로딩
        time.sleep(2)
        
        new_scroll_height = driver.execute_script('return document.querySelector("#_pcmap_list_scroll_container").scrollHeight')

        # 만약 새로운 데이터가 없다면
        if scroll_height == new_scroll_height:
            break;

    list = driver.find_elements(value='#_pcmap_list_scroll_container > ul > li', by=By.CSS_SELECTOR)

    for item in list:
        title = item.find_element(value='div.CHC5F > a.tzwk0 > div > div > span.TYaxT', by=By.CSS_SELECTOR).text
        title_arr.append(title)

    next_button = driver.find_element(by=By.CSS_SELECTOR, value='#app-root > div > div.XUrfU > div.zRM9F > a:nth-child(7)')
    next_button.click()

    # 다음 페이지 로딩
    time.sleep(2)

df = pd.DataFrame({
    'title': title_arr,
})

df.to_excel('맛집.xlsx')