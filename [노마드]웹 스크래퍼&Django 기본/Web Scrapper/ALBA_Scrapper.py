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
        companies = (link.find("span", {"class": "company"}).string).replace("/","&")
        links = link.a['href']
        pages.append({"brand":companies, "job_page":links})
        extract_SB_jobs(links,companies)
    print("-------All jobs have been scrapped successfully!-------")

def extract_SB_jobs(url,brand):
    print(f"Processing {brand} jobs...")
    brand_result = requests.get(url)
    SB_soup = BeautifulSoup(brand_result.text, "html.parser")
    normal_info = SB_soup.find(id="NormalInfo").find("tbody")
    rows = normal_info.find_all("tr", {"class":""})
    normal_infos = []
    for tr in rows:
        places = tr.find("td", {"class": "local first"})
        if places == None:
            print(f"There is no {brand} job now.")
            return #break 말고 return으로 해야 내용 빈 csv 안 생김
        else:
            places = (tr.find("td", {"class": "local first"})).get_text().replace('\xa0', ' ')
            titles = (tr.find("span", {"class": "company"})).get_text().lstrip()
            times = (tr.find("td", {"class": "data"})).get_text()
            pays = (tr.find("td", {"class": "pay"})).get_text()
            dates = (tr.find("td", {"class": "regDate last"})).get_text()
            normal_infos.append({"place": places, "title": titles, "time": times, "pay": pays, "date": dates})
    save_as_csv(normal_infos, brand)

def save_as_csv(nm_infos,brands):
    file = open(f"{brands}.csv", mode="w", encoding="UTF-8") #인코딩 설정 필요
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for jobs in nm_infos:
        writer.writerow(list(jobs.values()))
    print(f"{brands} jobs have been scrapped successfully!")

extract_SB_pages()


