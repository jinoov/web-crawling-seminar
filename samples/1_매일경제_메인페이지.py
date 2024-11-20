from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

# 맥에서 에러나는 경우에만 주석 해제
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

response = request.urlopen("https://www.mk.co.kr/")

soup = BeautifulSoup(response, "html.parser")

headline_1 = soup.select_one("h3#headline_1")

headline_1_text = headline_1.text.strip()

headline_2 = soup.select_one("h3#headline_2")

headline_2_text = headline_2.text.strip()

df = pd.DataFrame({"headline": [headline_1_text, headline_2_text]})

df.to_csv("output.csv")
