---
theme: seriph
background: '/images/background.jpg'
themeConfig:
  primary: '#560c7b'
  fontWeight: 500
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Web Crawling 101
mdc: true
fonts:
  sans: 'Pretendard'
  local: 'Pretendard'
---

# Web Crawling 101

2024-2 PoolC Seminar

---

# 세미나 소개

- 세미나장: 산업공학과 19학번 최진호
- 세미나 소요 시간: 2시간반 가량
- 출석체크는 끝날 때 진행합니다.
  - 중간에 나가게 된다면, 세미나장에게 꼭 말씀해주세요!
- 질문은 언제든 환영입니다. 자유롭게 질문해주세요.
- 뒷부분은 개인별 컴퓨터 환경의 영향을 조금 받을 수 있습니다. 😢

---

# 세미나 소개

- **웹 크롤링**의 전반적인 내용을 다룹니다.
  - 인터넷과 책에 충분히 많은 크롤링 관련 레퍼런스가 있습니다.
  - 크롤링 코드마저도 AI가 너무 잘 짜주는 현실... 😢
  - 해당 세미나에서는 **전반적인 흐름**과 **왜 이렇게 해야하는지**에 초점을 맞춥니다. 🔥

---

# Table Of Contents

1. 웹 크롤링의 기본 개념 🆙
2. 데이터를 정적으로 받아올 때
3. 데이터를 동적으로 받아올 때
4. Issues in Web Crawling 🆙

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #d7bde8; display: flex">
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

1. 데이터를 정적으로 받아오는가? ➡️ BeautifulSoup
2. 데이터를 동적으로 받아오는가? ➡️ Selenium

---

# 핵심 아이디어

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/python-intercept.png" alt="" width="500">
</div>

- Python이 마치 브라우저인 것처럼 행동하기

---

# 브러우저 요청과 파이썬 요청의 차이

<div style="padding: 10px; margin-top: 20px">
    <div style="display: flex; gap: 15px;">
        <img src="/images/sequential-requests.png" alt="" width="300">
        <ul>
            <li>
                <b>브라우저</b>는 순차적인 요청들을 모두 자동으로 실행<br/>
                <span style="font-weight: 300; color: #666">
                    이렇게 동작해야 사용자가 seamless하게 화면을 볼 수 있겠죠?
                </span>
            </li>
            <li>
                <b>파이썬</b>을 비롯한 대부분의 클라이언트들은 그렇게 동작하지는 않는다<br/>
                <span style="font-weight: 300; color: #666">
                    통상적인 웹사이트는 사용자가 브라우저 환경으로 접속할 것임을 가정함
                </span>
            </li>
        </ul>
    </div>
</div>

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #d7bde8; display: flex">
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
# window: .\venv\Scripts\activate

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

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #d7bde8; display: flex">
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
  - [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
- 근데 꼭 크롬 버전 정확하게 안맞추더라도 stable 다운받으면 웬만하면 다 맞긴해요 😅

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

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #d7bde8; display: flex">
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
  - User-Agent 정보를 브라우저껄로 변경해주면 뚫기 가능!
- 로그인해야 가져올 수 있는 데이터들은 token(고유 인증값)을 요구하기에 다소 어려울 수 있다.
  - 이걸 하려면 selenium으로 로그인 폼을 뚫어야합니다.
  - 만약 로그인에 CAPTCHA가 달려있다면 눈물.. 🥲
  - 이미지 인식 AI로 CAPTCHA를 풀려는 시도들이 계속 있기는 함. 그랬더니 AI에 안 뚫리는 CAPTCHA가 다시 출시되고 무한 반복..

<div style="padding: 10px; margin: 10px 0">
    <img src="/images/captcha.jpg" alt="" width="300">
</div>

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
- 다만, 상대측 서버에 과도한 부하를 주는 경우라든지 이용약관에 크롤링 금지 조항 등이 있는 경우, 정상영업 방해로 유죄로 판단되기도 하는 것 같음.
- 솔직히 판례마다 판결이 너무 달라서 뭐라 확신해서 말하기는 어렵다.. 🥲
  - (개인적인 생각) 미친듯이 실시간 봇을 돌린다든지 행위를 하지 않는 이상, 개인 사용에서는 큰 문제 없을 겁니다.

---

# 2. 이거 합법인가요?

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/robots-txt.png" alt="" width="100">
</div>

- `<사이트주소>/robots.txt`
- 크롤링 가능한 범위를 확인 가능.
- 지키면 바람직한 권고안.

---

# 3. IP 차단 우회하기

<div style="padding: 10px; margin: 20px 0">
    <img src="/images/proxy-server.png" alt="" width="300">
</div>

- 프록시 서버: 클라이언트에서 서버를 바로 찌르지 않고, 중간에 경유하는 서버.
- 크롤링 너무 많이하면 IP 차단을 당할 수도 있다. 프록시 서버를 경유하면, 내 컴퓨터의 IP 차단을 방지할 수 있다.

---

# 3. IP 차단 우회하기

<div style="padding: 10px; margin: 20px 0; display: flex; gap: 20px;">
    <img src="/images/free-proxy-list.png" alt="" width="300">
    <img src="/images/russian-rullet.jpeg" alt="" width="250">
</div>

- `proxy server list` 등을 검색하면 무료/유료 프록시서버 리스트들이 나온다.
- 프록시 서버 역시도 차단을 먹을 수 있기에 ^^; 여러개 돌려쓰는게 보통 권장된다.

---

# 4. 확장 가능성

1. 데이터 크롤링 ➡️ 데이터 전처리 ➡ ️AI 모델 돌리기
2. 데이터 크롤링 + 공공 API ➡️ 데이터 전처리 ➡ ️AI 모델 돌리기
3. 데이터 크롤링 ➡️ DB에 쌓기 ➡ 웹 서버 운영
4. 기타 등등

<div style="margin-top: 10px">
    <p style="color: #666;">크롤링 잘 익혀서 조별과제에서 사랑받는 팀원이 되자 👊</p>
</div>

---

<div style="position:fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #d7bde8; display: flex">
    <h1 style="color: white; margin: auto">끝.</h1>
</div>
