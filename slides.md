---
theme: seriph
themeConfig:
  primary: "#ff6f06"
  fontWeight: 500
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Git Basic Seminar
mdc: true
fonts:
  sans: "Noto Sans KR"
  local: "Noto Sans KR"
image: "https://unsplash.com/ko/%EC%82%AC%EC%A7%84/HLQDfaJUTVI"
---

# Web Crawling 101

---

# 발표자 소개

- 산업공학과 19학번 최진호
- 스타트업, 외주, ... 잡부로 일하는 중
- "웹이 미래다!"

---

# Table Of Contents

1. 웹 크롤링의 기본 개념
2. 데이터를 정적으로 받아올 때
3. 데이터를 동적으로 받아올 때
4. Issues in Web Crawling

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #ffbc97; display: flex">
    <h1 style="color: white; margin: auto">1. 웹 크롤링의 기본 개념</h1>
</div>

---

# Web

<div style="padding: 10px; margin-top: 20px">
    <img src="/images/client-server.png" alt="" width="500">
</div>

---

# Web

<div>
    <h2 style="font-size: 24px; font-weight: 600">A pretty dog barks.</h2>
    <ul style="margin-top: 10px">
        <li>dog ➡️ HTML</li>
        <li>pretty ➡️ CSS</li>
        <li>bark ➡️ JavaScript</li>
    </ul>
</div>
<div style="margin-top: 60px">
    <p>네이버에서 <code>f12</code>를 눌러보자</p>
</div>

---

# Data in Web

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/client-server.png" alt="" width="500">
</div>

1. 데이터를 정적으로 받아오는가?  ➡️  BeautifulSoup
2. 데이터를 동적으로 받아오는가?  ➡️  Selenium

---

# Python이 마치 브라우저인 것처럼 행동하기 

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/python-intercept.png" alt="" width="500">
</div>

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #ffbc97; display: flex">
    <h1 style="color: white; margin: auto">2. 데이터를 정적으로 받아올 때</h1>
</div>

---

# 원리

<div style="padding: 10px; margin-top: 20px">
    <div style="display: flex; gap: 15px;">
        <img src="/images/response-parsing.png" alt="" width="500">
        <ul>
            <li>서버에서 내려주는 응답은 단순 텍스트.</li>
            <li>해당 텍스트에 생기를 넣어준다(parsing).</li>
            <li>원하는 데이터를 가져온다!</li>
        </ul>
    </div>
</div>

---

# 0. 환경설정

```shell
# 가상 환경 만들기
python -m venv venv

source ./venv/bin/activate
# window: ./venv/Scripts/activate

# vscode
# - 파이썬 관련 익스텐션들 설치
# - `ctrl(cmd) + shift + p` -> Python: Select Interpreter -> venv 설정

# 패키지 설치
pip install beautifulsoup4 selenium pandas

# 패키지 정보 남기기
pip freeze > requirements.txt
```

---

# 1. 매일경제 헤드라인 & 상세페이지 읽어오기

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/mk-headline.png" alt="" width="500">
</div>

---

# 2. 네이버 증권 top 종목들 시세 읽어오기

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/naver-finance-top-items.png" alt="" width="400">
</div>

---

# 요약

- `urllib`을 이용해 서버로부터 응답을 받아온다.
- `beautifulsoup4`를 이용해 받아온 응답을 파싱한다.
- `soup.select` 등을 이용해 요소 선택 및 텍스트 추출.

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #ffbc97; display: flex">
    <h1 style="color: white; margin: auto">3. 데이터를 동적으로 받아올 때</h1>
</div>

---

# 원리

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/python-control-chrome.png" alt="" width="500">
</div>

---

# 0. 환경설정
- 크롬 버전 확인하기
    - [chrome://settings/help](chrome://settings/help)
- 크롬 버전에 해당하는 driver 다운로드 받아서 디렉토리(폴더)에 넣어주기
    - [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/driver.png" alt="" width="300">
</div>
---

# 1. 매일경제 경제란 더보기 버튼

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/mk-more-button.png" alt="" width="500">
</div>

---

# 2. 네이버지도에서 신촌맛집 검색하기

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/sinchon-restaurant.png" alt="" width="500">
</div>

---

# 요약

- web driver 설치 후 `selenium`을 이용해 test용 chrome을 띄운다.
- `driver.find_element` 등의 함수를 이용해 요소를 선택 및 조작.
- 중간중간 로딩에 걸리는 시간은 `time.sleep` 등으로 대응.
- 무한스크롤 & 페이지네이션 신경쓰기.

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #ffbc97; display: flex">
    <h1 style="color: white; margin: auto">4. Issues in Web Crawling</h1>
</div>

---

# 1. 그냥 데이터 직접 가져오면 안되나요?

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/python-dynamic.png" alt="" width="300">
</div>

- 자바스크립트에서 가져오는 **동적으로 가져오는 데이터**를 파이썬에서 가져오자!

---

# 1. 그냥 데이터 직접 가져오면 안되나요?

- User-Agent 정보(브라우저에서 호출했는지, 파이썬에서 호출했는지)를 확인하는 경우들이 종종 있다.
- 로그인해야 가져올 수 있는 정보는 힘들 수 있다.

---

# 1. 그냥 데이터 직접 가져오면 안되나요?

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/yonsei-mileage.png" alt="" width="700">
</div>

---

# 2. 이거 합법인가요?

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/crawling-legal.png" alt="" width="300">
</div>

- 이미 오픈된 정보이기에 일반적으로 무죄로 판단.
- 다만, 상대측 서버에 과도한 부하를 주는 경우 정상영업 방해로 유죄로 판단될 수 있다.
- (법알못이라 자세히는 모릅니다...)

---

# 2. 이거 합법인가요? 

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/robots-txt.png" alt="" width="100">
</div>

- `<사이트주소>/robots.txt`
- 크롤링 가능한 범위를 확인 가능.
- 지키면 바람직한 권고안.

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #ffbc97; display: flex">
    <h1 style="color: white; margin: auto">끝.</h1>
</div>