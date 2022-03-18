import os
import requests

def restart_Y_N():
  YN = input("Do you want start over? y/n ") #input()의 위치 유의
  if YN.lower() == "y":
      os.system("clear") #콘솔창 클리어 코드(리눅스 기준)
      is_it_down()
  elif YN.lower() == "n":
    print("k. bye!")
  else:
    print("That's not a valid answer")
    restart_Y_N()

def preprocess_url(input=""):
  input = input.lower()
  input = input.replace(' ','') #.strip()안먹히는데??
  URLs = input.split(',') #,를 구분으로 쪼갠 리스트 생성
  HTTP = "http://"
  for URL in URLs: #주의) 여기서 URL은 URLs의 아이템을 **복사한 값**을 전달한 것 뿐!!
    # URL=변경할 내용으로 한다 해도 실제 리스트의 항목에는 영향을 주지 못한다
    isHTTP = "http" in URL #boolean값을 변수에 담아야 if문에서 쓸 수 있다!
    #조건을 "http"로 해줘야 "http://", "https://" 모두 통과시킬 수(True)있다!
    if isHTTP is False:
      URLs[URLs.index(URL)] = HTTP+URL #실제 리스트 item의 값을 변경하고 싶다면 요렇게(인덱스 사용) 해야한다
  return URLs

def is_it_down():
  print("Welcome to IsItDown.py!")
  url = input("Please write a URL or URLs you want to check. (Seperated by comma)\n")
  URLs = preprocess_url(url)
  for URL in URLs:
    try:
      URL_status = requests.get(URL).status_code
      if URL_status == 200:
        print(f"{URL} is up!")
      else:
        print(f"{URL} is down!")
    except:
      valid_url_dot = "." in URL
      valid_url_slash = "/" in URL
      valid_url_colon = ":" in URL
      isHTTP = "http://" in URL
      if valid_url_dot is False and isHTTP is True:
        print(f"{URL.strip('http://')} is not a valid url")
      elif valid_url_dot is False:
        print(f"{URL.strip('http://''https://')} is not a valid url")
      elif valid_url_slash or valid_url_colon is False:
        print(f"{URL} is not a valid url")
      else:
        print(f"{URL} is down!")
  restart_Y_N()

is_it_down()
