import time
import requests
from bs4 import BeautifulSoup
from requests.api import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

interval = 2
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
browser.maximize_window()   # 페이지 크기 최대화

# 페이지 이동
url = "https://www.7-eleven.co.kr/product/presentList.asp"
browser.get(url)

# "+"버튼 찾아서 클릭(이때의 xpath는 아래와 같음)
time.sleep(interval)
elem = browser.find_element_by_xpath("//*[@id='listUl']/li[15]/a")
elem.click()
time.sleep(interval)

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 1+1 페이지 끝까지 내리기
while True:
    # +버튼 찾기
    elem = browser.find_element_by_xpath("//*[@id='moreImg']/a")
    # +버튼 클릭
    elem.send_keys(Keys.ENTER)
    # 페이지 로딩 대기
    time.sleep(interval)

    print("이전 높이 : ", prev_height)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 높이가 같으면 +버튼이 눌리지 않는 것이므로 종료
    if prev_height == curr_height:
        break
    
    print("이후 높이 : ", curr_height)
    
    # 이전 높이 갱신
    prev_height = curr_height
    
     # 페이지 로딩 대기
    time.sleep(interval)
    
soup = BeautifulSoup(browser.page_source, "lxml")
goods = soup.find_all("div", attrs={"class":"name"})      # 전체 상품
prices = soup.find_all("div", attrs={"class":"price"})    # 전체 상품 가격
images = soup.find_all("img", attrs={"height":130})          # 전체 상품 이미지


# 각 행사 상품 이미지 경로 저장
for idx, image in enumerate(images):
    image_url = image["src"]
    
    with open("seven_11_url.txt", "a") as f:
        f.write("https://www.7-eleven.co.kr/" + image_url + "\n")
        
print("경로 저장 완료")


for idx, good in enumerate(goods):
    # 상품 이름 : 가격 출력
    print(good.get_text() + " : " + prices[idx].get_text())
    
    # 상품 이름 저장
    with open('seven_11_name.txt','a') as f1:
        f1.write(good.get_text() + '\n')
    
    # 상품 가격 저장
    with open('seven_11_price.txt','a') as f2:
        f2.write(prices[idx].get_text()[1:-1] + '\n')
        
print("Seven 1+1 상품명, 가격, url 저장 완료")


# ----------------------------------------------------------------

# 2+1 버튼
elem = browser.find_element_by_link_text("2+1")
elem.click()

# +버튼
time.sleep(interval)
elem = browser.find_element_by_xpath("//*[@id='listUl']/li[15]/a")
elem.click()
time.sleep(interval)

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

index = 0
# 2+1 페이지 끝까지 내리기
while True:
    # +버튼 찾기
    elem = browser.find_element_by_xpath("//*[@id='moreImg']/a")
    
    if not elem:
        break
    
    # +버튼 클릭
    elem.send_keys(Keys.ENTER)
    index = index + 1
    
    # 페이지 로딩 대기
    time.sleep(interval)

    print("이전 높이 : ", prev_height)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 높이가 같으면 +버튼이 눌리지 않는 것이므로 종료
    if prev_height == curr_height:
        break
    
    print("이후 높이 : ", curr_height)
    
    # 이전 높이 갱신
    prev_height = curr_height
    
     # 페이지 로딩 대기
    time.sleep(interval)

print("총 ", index, "번 눌렀다.")

soup = BeautifulSoup(browser.page_source, "lxml")
goods = soup.find_all("div", attrs={"class":"name"})      # 전체 상품
prices = soup.find_all("div", attrs={"class":"price"})    # 전체 상품 가격
images = soup.find_all("img", attrs={"height":130})          # 전체 상품 이미지


# 각 행사 상품 이미지 경로 저장
for idx, image in enumerate(images):
    image_url = image["src"]
    
    with open("seven_11_url.txt", "a") as f:
        f.write("https://www.7-eleven.co.kr/" + image_url + "\n")
        
print("경로 저장 완료")


for idx, good in enumerate(goods):
    # 상품 이름 : 가격 출력
    print(good.get_text() + " : " + prices[idx].get_text())
    
    # 상품 이름 저장
    with open('seven_11_name.txt','a') as f1:
        f1.write(good.get_text() + '\n')
    
    # 상품 가격 저장
    with open('seven_11_price.txt','a') as f2:
        f2.write(prices[idx].get_text()[1:-1] + '\n')
        
print("Seven 2+1 상품명, 가격, url 저장 완료")