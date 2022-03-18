import os
import requests

def restart_Y_N():
  YN = input("Do you want start over? y/n ") #위치 유의
  if YN.lower() == "y":
      os.system("clear") #콘솔창 클리어 코드(리눅스 기준)
      is_it_down()
  elif YN.lower() == "n":
    print("k. bye!")
    return
  else:
    print("That's not a valid answer")
    restart_Y_N()

def is_it_down():
  print("Welcome to IsItDown.py!")
  URL = input("Please write a URL or URLs you want to check. (Seperated by comma)\n")
  URLs = [URL]
  for URL in URLs:
    URL_status = requests.get(URL).status_code
    if URL_status == 200:
      print(f"{URL} is up!")
    else:
      print(f"{URL} is down!")
  restart_Y_N()

is_it_down()

