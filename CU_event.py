import time
import requests
from bs4 import BeautifulSoup
from requests.api import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# interval = 3
# browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
# url = "https://cu.bgfretail.com/event/plus.do?category=event"
# browser.get(url)

# # 1+1 버튼 클릭
# time.sleep(interval)
# elem = browser.find_element_by_class_name("eventInfo").find_element_by_link_text("1+1").click()
# time.sleep(interval)

# while True:
#     time.sleep(interval)
#     try:
#         # 더보기 버튼 받아오기
#         elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='contents']/div[1]/div[2]/div/div[1]/a")))
#     # 더보기 버튼 없으면 종료    
#     except Exception:
#         print("타임 아웃")
#         break
        
#     # 더보기 버튼 클릭
#     elem.click()

# soup = BeautifulSoup(browser.page_source, "lxml")
# goods = soup.find_all("p", attrs={"class":"prodName"})      # 전체 상품
# prices = soup.find_all("p", attrs={"class":"prodPrice"})    # 전체 상품 가격
# images = soup.find_all("img", attrs={"width":180})          # 전체 상품 이미지

# # # 각 행사 상품 이미지 파일로 저장
# # for idx, image in enumerate(images):
# #     image_url = image["src"]
    
# #     image_res = requests.get(image_url)
# #     image_res.raise_for_status()
    
# #     with open("img_1+1_{}.jpg".format(idx), "wb") as f:
# #         f.write(image_res.content)
        
# #     if idx==3:
# #         break

# # 각 행사 상품 이미지 경로 저장
# with open("cu_11_link.txt", "w", encoding='utf-8') as f:

#     for idx, image in enumerate(images):
#         image_url = image["src"]
#         f.write(image_url + "\n")
        
# print("경로 저장 완료")

# with open('cu_11_name.txt','w', encoding='utf-8') as f1:
#     with open('cu_11_price.txt','w', encoding='utf-8') as f2:

#         for idx, good in enumerate(goods):
#             # 상품 이름 : 가격 출력
#             print(good.get_text() + " : " + prices[idx].get_text())
            
#             # 상품 이름 저장
#             f1.write(good.get_text() + '\n')
            
#             # 상품 가격 저장
#             f2.write(prices[idx].get_text() + '\n')
# print("저장 완료")

# # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2+1 상품

interval = 3
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
url = "https://cu.bgfretail.com/event/plus.do?category=event"
browser.get(url)

# 2+1 버튼 클릭
elem = browser.find_element_by_class_name("eventInfo").find_element_by_link_text("2+1").click()
time.sleep(interval)
interval = 15
while True:
    time.sleep(interval)
    try:
        # 더보기 버튼 받아오기
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='contents']/div[1]/div[2]/div/div[1]/a")))
    except:
        break
    
    # 더보기 버튼이 없으면 종료
    if not elem:
        break
    
    # 더보기 버튼 클릭
    elem.click()

soup = BeautifulSoup(browser.page_source, "lxml")
goods = soup.find_all("p", attrs={"class":"prodName"})    # 상품
prices = soup.find_all("p", attrs={"class":"prodPrice"})  # 가격
images = soup.find_all("img", attrs={"width":180})          # 이미지


# 각 행사 상품 이미지 경로 저장
with open("cu_21_link.txt", "w", encoding='utf-8') as f:
    for idx, image in enumerate(images):
        image_url = image["src"]
        f.write(image_url + "\n")
        
print("경로 저장 완료")

with open('cu_21_name.txt','w', encoding='utf-8') as f1:
    with open('cu_21_price.txt','w', encoding='utf-8') as f2:
        for idx, good in enumerate(goods):
            # 상품 이름 : 가격 출력
            print(good.get_text() + " : " + prices[idx].get_text())
            
            # 상품 이름 저장
            f1.write(good.get_text() + '\n')
            
            # 상품 가격 저장
            f2.write(prices[idx].get_text() + '\n')

print("저장 완료")
