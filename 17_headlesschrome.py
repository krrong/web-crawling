from selenium import webdriver

# 크롬창을 띄우지 않고 백그라운드로 동작
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies"
browser.get(url)

import time
interval = 2 # 2초에 한 번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)
    
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if prev_height == curr_height:
        break
    
    prev_height = curr_height
    
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")  # 스크린 샷 찍기

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"})
    
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title)
        continue
    
    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()
    
    # 링크
    link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    # 올바른 링크 : http://play.google.com + link
    
    # get_text()가 없을 수도 있어서 분류
    if title:
        title = title.get_text()
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "http://play.google.com" + link)
    print("-"*100)
    
browser.quit()