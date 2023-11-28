from urllib.request import urlopen
import json

response = urlopen('https://weather.naver.com/today/api/nation/20231128/now')

obj = json.loads(response.read())

print(obj)