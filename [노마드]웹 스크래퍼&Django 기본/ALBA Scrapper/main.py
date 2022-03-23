from bs4 import BeautifulSoup
import requests

main_result = requests.get("http://www.alba.co.kr/")
soup = BeautifulSoup(main_result.text, "html.parser")
main_super_brand = soup.find(id="MainSuperBrand")
super_brands = main_super_brand.find("ul", {"class": "goodsBox"})
super_brand_jobs = super_brands.find_all('li')

def extract_SB_companies():
    companies = []
    for company in super_brand_jobs[:-1]:
        company_names = (company.find("span", {"class": "company"}).string)
        companies.append(company_names)
    print(companies)

def extract_SB_links():
    links = []
    for link in super_brand_jobs[:-1]:
        links.append(link.a['href'])
    print(links)

extract_SB_companies()
extract_SB_links()




