from urllib.request import urlopen, Request
import json

URL = 'https://weather.naver.com/today/api/nation/20231128/now'
USER_AGENT = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'"

response = urlopen(Request(url=URL, headers={'User-Agent': USER_AGENT}))

obj = json.loads(response.read())

data = obj['N04940320']
print(data['regionName'], data['wetrTxt'], data['tmpr'])