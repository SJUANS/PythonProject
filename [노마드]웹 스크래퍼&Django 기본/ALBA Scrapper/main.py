import os
import csv
from bs4 import BeautifulSoup
import requests

os.system("clear")
alba_url = "http://www.alba.co.kr"

main_result = requests.get(alba_url)
soup = BeautifulSoup(main_result.text, "html.parser")
main_super_brand = soup.find(id="MainSuperBrand")
super_brands = main_super_brand.find("ul", {"class": "goodsBox"})
super_brand_jobs = super_brands.find_all('li')

def extract_SB_pages():
    pages = []
    for link in super_brand_jobs[:-1]:
        companies = (link.find("span", {"class": "company"}).string) #단일 요소에서 문자열 빼낼 때는 string
        links = link.a['href']
        pages.append({"brand":companies, "job_page":links})
        # file = open(f"{companies}.csv", mode="w")
        # 브랜드명에 /들어가면 에러 나는거 디버깅해야 함
    return pages

def extract_SB_jobs(): #나중에 pages에서 링크 받아와서 인자로 넣어야 함
    #place,title(지점),time,pay,date
    url = "https://mmthcoffee.alba.co.kr/" #임시
    brand_result = requests.get(url)
    SB_soup = BeautifulSoup(brand_result.text, "html.parser")
    normal_info = SB_soup.find(id="NormalInfo").find("tbody")
    rows = normal_info.find_all("tr", {"class":""})

    for tr in rows:
        normal_infos = []
        places = (tr.find("td", {"class": "local first"})).get_text() #여러 요소에서 문자열 빼낼 때는 get_text()
        titles = (tr.find("span", {"class":"company"})).get_text()
        times = (tr.find("td", {"class":"data"})).get_text()
        pay_text = (tr.find("td", {"class":"pay"})).get_text()
        pays = f'"{pay_text}"'
        dates = (tr.find("td", {"class":"regDate last"})).get_text()

        print(places,titles,times,pays,dates)

extract_SB_jobs()


