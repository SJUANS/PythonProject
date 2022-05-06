import json
import re #파이썬 정규표현식 라이브러리
from bs4 import BeautifulSoup
import requests

cocktail_detail_Triple_Daiquiri = "https://www.diffordsguide.com/cocktails/recipe/4809/triple-daiquiri"
page_Triple_Daiquiri = requests.get(cocktail_detail_Triple_Daiquiri)
soup = BeautifulSoup(page_Triple_Daiquiri.text, "html.parser")

#크롤링으로 수집 가능 정보↓
cocktail_info = soup.find("script", {"type": "application/ld+json"})
string_cocktail_info = cocktail_info.text #HTML 요소 내 JSON으로 작성된 부분 문자열화
dict_result = json.loads(string_cocktail_info) #문자열화한 결과를 다시 JSON으로 변환

#칵테일 이름 o
Name = dict_result['name']
#이미지url o
Img = dict_result['image']
#부재료(=가니쉬) o
Garnish = soup.select("#sticky-anchor > div > div > div.cell.auto.divide-right-large > div > article > div > div:nth-child(2) > p")
Garnish = Garnish[0].text
#맛
#상세도수 o
Alc_by_vol = soup.select("#sticky-anchor > div > div > div.cell.auto.divide-right-large > div > article > div > div:nth-child(14) > ul > li:nth-child(2)")
AbV = Alc_by_vol[0].text
Floats_in_AbV = re.findall("\d+.\d+",AbV) #정규표현식으로 AbV라는 문자열 안에 있는 숫자 두개 추출
AbV = Floats_in_AbV[0]
#레시피 재료 o
Ingredients = dict_result['recipeIngredient']
#레시피 o
Recipe = dict_result['recipeInstructions'][0]['text']

# print(Name,Img,Ingredients,Recipe)

