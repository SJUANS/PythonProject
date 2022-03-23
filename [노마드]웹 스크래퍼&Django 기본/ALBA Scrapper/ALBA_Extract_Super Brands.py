from bs4 import BeautifulSoup
import requests

main_result = requests.get("http://www.alba.co.kr/")
soup = BeautifulSoup(main_result.text, "html.parser")
main_super_brand = soup.find(id="MainSuperBrand")
super_brands = main_super_brand.find("ul", {"class":"goodsBox"})
super_brand_jobs = super_brands.find_all('li')

def extract_SB_links():
    for link in super_brand_jobs[:-1]:
        links = []
        links.append(link.a['href'])
    return links

