from urllib import request
from bs4 import BeautifulSoup

URL = 'https://www.mk.co.kr/news/politics/10885534'
response = request.urlopen(URL)

soup = BeautifulSoup(response.read(), 'html.parser')

title = soup.select_one('#container > section > div.news_detail_head_group.type_none_bg > section > div > div > div > h2')

paragraph_list = soup.select('#container > section > div.news_detail_body_group > section > div.min_inner > div.sec_body > div:nth-child(1) > p')

result = ''

for paragraph in paragraph_list:
    result += paragraph.text

print('----제목----')
print(title.text.strip())
print('----본문-----')
print(result)