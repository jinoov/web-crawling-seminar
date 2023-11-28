from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

# 메인페이지
URL = 'https://www.mk.co.kr'
response = request.urlopen(URL)

soup = BeautifulSoup(response.read(), 'html.parser')

headline_1 = soup.select_one('#headline_1')
text_1 = headline_1.text.strip()

headline_2 = soup.select_one('#container > section > div.mk_head_news_group > div > div > div.col.main_col > section > div > ul > li.col.col_12.news_node.headline_news_node > div > div > ul > li:nth-child(1) > a')
text_2 = headline_2.text.strip()

headline_3 = soup.select_one('#container > section > div.mk_head_news_group > div > div > div.col.main_col > section > div > ul > li.col.col_12.news_node.headline_news_node > div > div > ul > li:nth-child(2) > a')
text_3 = headline_3.text.strip()

df = pd.DataFrame({
    '본문': [text_1, text_2, text_3],
})

df.to_excel('헤드라인 뉴스목록.xlsx')