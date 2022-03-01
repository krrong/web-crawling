import time
import requests
from bs4 import BeautifulSoup
from requests.api import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

interval = 3
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
url = "http://gs25.gsretail.com/gscvs/ko/products/event-goods#;"

browser.get(url)
time.sleep(interval)
goods = list()
prices = list()
links = list()
soup = BeautifulSoup(browser.page_source, "lxml")
lastIndex = 39 # 따로 마지막 페이지를 알릴 수 없어서 직접 수정 필요
curIndex = 0

# 매 페이지에서 상품 정보 가져오기
while True:
    if curIndex == lastIndex:
        break
    curIndex += 1
    
    soup = BeautifulSoup(browser.page_source, "lxml")
    # pageBtn = soup.find("div", attrs={"class":"paging"}).find("span", attrs={"class","num"}).find_all("a", attrs={"title":"내용보기"}) # 페이지 버튼(1~10)

    pageGoods = soup.find("ul", attrs={"class":"prod_list"}).find_all("p", attrs={"class":"tit"})
    pagePrices = soup.find("ul", attrs={"class":"prod_list"}).find_all("span", attrs={"class":"cost"})
    pageLinks = soup.find("ul", attrs={"class":"prod_list"}).find_all("img")

    try:
        for i in range(0, len(pageGoods)):
            goods.append(pageGoods[i].get_text())
            prices.append(pagePrices[i].get_text())
            links.append(pageLinks[i])
    except:
        print(curIndex, '페이지 확인 필요합니다.')

    # print(goods)
    # print(prices)
    # print(links)

    next = browser.find_element_by_xpath("//*[@id='contents']/div[2]/div[3]/div/div/div[1]/div/a[3]")
    
    next.click()
    time.sleep(interval / 2)


with open("gs_11_link.txt", "w", encoding='utf-8') as f:

    # 각 행사 상품 이미지 경로 저장
    for idx, link in enumerate(links):
        imageLink = link['src']
        
        f.write(imageLink + '\n')
        
print("경로 저장 완료")


with open('gs_11_name.txt','w', encoding='utf-8') as f1:
    with open('gs_11_price.txt','w', encoding='utf-8') as f2:

        # 각 행사 상품 이름, 가격 저장
        for idx, good in enumerate(goods):
            # 상품 이름 : 가격 출력
            print(good + " : " + prices[idx])
            
            # 상품 이름 저장
            f1.write(good + '\n')
            
            # 상품 가격 저장
            f2.write(prices[idx] + '\n')
        
print(len(goods), "개 1+1 상품 저장 완료")

# ---------------------------------------------------------------------------------------------------------------------------------------
# 2 + 1 상품

# interval = 3
# browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
url = "http://gs25.gsretail.com/gscvs/ko/products/event-goods#;"

browser.get(url)
time.sleep(interval)

goods = list()
prices = list()
links = list()

# 2+1 페이지로 이동
elem = browser.find_element_by_xpath("//*[@id='contents']/div[2]/div[3]/div/div/ul/li[2]/span")
elem.click()
time.sleep(interval)

lastIndex = 113 # 따로 마지막 페이지를 알릴 수 없어서 직접 수정 필요
curIndex = 0

# 매 페이지에서 상품 정보 가져오기
while True:
    if curIndex == lastIndex:
        break
    curIndex += 1
    
    soup = BeautifulSoup(browser.page_source, "lxml")

    pageGoods = soup.find("ul", attrs={"class":"prod_list"}).find_all("p", attrs={"class":"tit"})
    pagePrices = soup.find("ul", attrs={"class":"prod_list"}).find_all("span", attrs={"class":"cost"})
    pageLinks = soup.find("ul", attrs={"class":"prod_list"}).find_all("img")

    try:
        for i in range(0, len(pageGoods)):
            goods.append(pageGoods[i].get_text())
            prices.append(pagePrices[i].get_text())
            links.append(pageLinks[i])
    except:
        print(curIndex, '페이지 확인 필요합니다.')

    next = browser.find_element_by_xpath("//*[@id='contents']/div[2]/div[3]/div/div/div[2]/div/a[3]")
    
    next.click()
    time.sleep(interval / 2)


with open("gs_21_link.txt", "w", encoding='utf-8') as f:

    # 각 행사 상품 이미지 경로 저장
    for idx, link in enumerate(links):
        imageLink = link['src']
        
        f.write(imageLink + '\n')
        
print("경로 저장 완료")

with open('gs_21_name.txt','w', encoding='utf-8') as f1:
    with open('gs_21_price.txt','w', encoding='utf-8') as f2:

        # 각 행사 상품 이름, 가격 저장
        for idx, good in enumerate(goods):
            # 상품 이름 : 가격 출력
            print(good + " : " + prices[idx])
            
            # 상품 이름 저장
            f1.write(good + '\n')
            
            # 상품 가격 저장
            f2.write(prices[idx] + '\n')
        
print(len(goods), "개 2+1 상품 저장 완료")
