import json

from bs4 import BeautifulSoup
import requests

cocktail_detail_Triple_Daiquiri = "https://www.diffordsguide.com/cocktails/recipe/4809/triple-daiquiri"
page_Triple_Daiquiri = requests.get(cocktail_detail_Triple_Daiquiri)
soup = BeautifulSoup(page_Triple_Daiquiri.text, "html.parser")

#크롤링으로 수집 가능 정보↓
cocktail_info = soup.find("script", {"type": "application/ld+json"})
string_cocktail_info = cocktail_info.text #HTML 요소 내 JSON을 문자열화
dict_result = json.loads(string_cocktail_info) #문자열화한 결과를 다시 JSON으로 변환

print(dict_result)

#칵테일 이름 o

#Name =
#이미지url
#부재료(=가니쉬)
#맛
#상세도수
#레시피 재료
#레시피 o