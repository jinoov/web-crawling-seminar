from urllib import request
from bs4 import BeautifulSoup

# 상세페이지
URL = 'https://www.mk.co.kr'
response = request.urlopen(URL)

soup = BeautifulSoup(response.read(), 'html.parser')

link = soup.select_one('#container > section > div.mk_head_news_group > div > div > div.col.main_col > section > div > ul > li.col.col_12.news_node.headline_news_node > div > a')

DETAIL_PAGE_URL = URL + link.attrs['href']
response_detail = request.urlopen(DETAIL_PAGE_URL)

soup_detail = BeautifulSoup(response_detail.read(), 'html.parser')

paragraph_list = soup_detail.select('#container > section > div.news_detail_body_group > section > div.min_inner > div.sec_body > div:nth-child(1) > p')

result = ''

for paragraph in paragraph_list:
    result += paragraph.text

print(result)