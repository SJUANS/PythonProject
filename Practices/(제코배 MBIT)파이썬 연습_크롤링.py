import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%B5%9C%EC%8B%A0%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84"
response = requests.get(url)
response.encoding = "utf-8"
html = response.text

soup = BeautifulSoup(html, "html.parser")

영화리스트 = soup.select('.name') #name 클래스 검색
for 순위, 영화명 in enumerate(영화리스트, 1): #이건 뭐지????
    print(순위, 영화명.text)

#실행하면 50 이후로는 지저분함 나중에 정리할 수 있는 방법 있음 찾아보기