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
        companies = (link.find("span", {"class": "company"}).string)
        links = link.a['href']
        pages.append({"brand":companies, "job_page":links})
    print(pages)

extract_SB_pages()



