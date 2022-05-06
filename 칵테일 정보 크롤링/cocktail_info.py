from bs4 import BeautifulSoup
import requests

cocktail_detail_Triple_Daiquiri = "https://www.diffordsguide.com/cocktails/recipe/4809/triple-daiquiri"
page_Triple_Daiquiri = requests.get(cocktail_detail_Triple_Daiquiri)
soup = BeautifulSoup(page_Triple_Daiquiri.text, "html.parser")

print(soup)

#크롤링으로 수집 가능 정보↓
#칵테일 이름
#이미지url
#부재료(=가니쉬)
#맛
#상세도수
#레시피