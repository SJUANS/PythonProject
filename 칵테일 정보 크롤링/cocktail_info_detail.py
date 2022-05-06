import json
import re #파이썬 정규표현식 라이브러리
from bs4 import BeautifulSoup
import requests

def extract_cocktail_collection(url):
    page_detail = requests.get(url)
    soup = BeautifulSoup(page_detail.text, "html.parser")

    # 크롤링으로 수집 가능 정보↓
    # <script>태그 안 JSON에 저장된 정보
    cocktail_page = soup.find("script", {"type": "application/ld+json"})
    string_cocktail_page = cocktail_page.text  # HTML 요소 내 JSON으로 작성된 부분 문자열화
    dict_result = json.loads(string_cocktail_page)  # 문자열화한 결과를 다시 JSON으로 변환

    # 칵테일 이름
    Name = dict_result['name']
    # 이미지url
    Img = dict_result['image']
    # 부재료(=가니쉬)
    cells = soup.find_all("div", {"class": "cell"})
    paragraphs = []
    for cell in cells:
        p = cell.find("p", {"class":""})
        if p is not None:
            paragraphs.append(p)
    Garnish = paragraphs[0].text
    # 맛
    try:
        Flavor_chart = soup.find("div", {"class": "grid-x align-justify"}).find("img")
        Flavor = Flavor_chart["alt"]
    except:
        Flavor = "Undefined" #flavor 척도 없는 경우의 예외 처리
    # 상세도수
    Alcohol_content = soup.find("ul", {"class": "no-margin-bottom"}).find_all("li")
    AbV = Alcohol_content[1].get_text()
    Floats_in_AbV = re.findall("\d+.\d+", AbV)  # 정규표현식으로 AbV라는 문자열 안에 있는 숫자 추출
    Alc_by_vol = float(Floats_in_AbV[0])  # 추출한 숫자의 자료형: 문자열>실수 로 변환
    # 도수(범주형)
    AbV_level = "Undefined"
    if Alc_by_vol <= 10:
        AbV_level = "1"
    elif Alc_by_vol <= 20:
        AbV_level = "2"
    elif Alc_by_vol <= 30:
        AbV_level = "3"
    elif Alc_by_vol <= 40:
        AbV_level = "4"
    elif Alc_by_vol <= 50:
        AbV_level = "5"
    elif Alc_by_vol >= 51:
        AbV_level = "6"
    # 레시피 재료
    Ingredients = dict_result['recipeIngredient']
    # 레시피
    Recipe = dict_result['recipeInstructions'][0]['text']

    cocktail_data = {
        "이름" : Name,
        "썸네일" : Img,
        "부재료" : Garnish,
        "맛" : Flavor,
        "도수" : AbV_level,
        "상세 도수" : Alc_by_vol,
        "재료" : Ingredients,
        "레시피" : Recipe
    }
    with open(f'page_3_{Name}.json', 'w', encoding="utf-8") as f:
        json.dump(cocktail_data, f, indent="\t", ensure_ascii=False)
    print(f"...Information of {Name} was collected")
