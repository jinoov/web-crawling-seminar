from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://finance.naver.com/'

response = request.urlopen(URL)

soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='cp949')

rows = soup.select('#_topItems1 > tr')

name_list = []
total_value_list = []
change_value_list = []
percentage_list = []

for row in rows:
    name = row.select_one('th > a').text.strip()
    total_value = row.select_one('td:nth-child(2)').text.strip()
    change_value = row.select_one('td:nth-child(3)').text.strip()
    percentage = row.select_one('td:nth-child(4)').text.strip()

    name_list.append(name)
    total_value_list.append(total_value)
    change_value_list.append(change_value)
    percentage_list.append(percentage)

df = pd.DataFrame({
    '종목명': name_list,
    '시가총액': total_value_list,
    '변동액': change_value_list,
    '변동률': percentage_list,
})

df.to_excel('주식.xlsx')