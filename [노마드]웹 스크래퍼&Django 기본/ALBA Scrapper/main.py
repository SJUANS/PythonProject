from bs4 import BeautifulSoup
import requests

main_result = requests.get("http://www.alba.co.kr/")
soup = BeautifulSoup(main_result.text, "html.parser")
main_super_brand = soup.find(id="MainSuperBrand")
super_brands = main_super_brand.find("ul", {"class": "goodsBox"})
super_brand_jobs = super_brands.find_all('li')

def extract_SB_pages():
    pages = []
    for link in super_brand_jobs[:-1]:
        companies = (link.find("span", {"class": "company"}).string)
        links = link.a['href']
        pages.append({"brand":companies, "job_link":links})
    print(pages)

extract_SB_pages()



