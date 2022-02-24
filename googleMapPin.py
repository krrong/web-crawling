# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import pyperclip

# interval = 2
# options = webdriver.ChromeOptions()
# # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe", options=options)

# url = "https://www.google.com/maps/?hl=ko"
# browser.get(url)
# time.sleep(interval)

import csv

file = open('data.csv', 'r', encoding='utf-8')
buildingList = list()
addressList = list()
reader = csv.reader(file)

# D(건물명) 읽어오기
for line in reader:
    building = line[3]
    index = 0
    building = building.split("(")[0]
    # print(building)
    buildingList.append(building)
file.close()

# G(주소) 읽어오기
for line in reader:
    addr = line[4]
    index = 0
    addr = addr.split("(")[0]
    # print(addr)
    addressList.append(addr)
file.close()

# # 로그인 버튼 클릭
# elem = browser.find_element_by_xpath("//*[@id='gb_70']")
# print("로그인 버튼 찾기 완료")
# elem.click()
# print("로그인 버튼 클릭 완료")

# # 아이디 입력, 다음 버튼 클릭
# time.sleep(interval)
# elem = browser.find_element_by_id("identifierId")
# print("아이디 입력 칸 찾기 완료")
# elem.send_keys("kik2135@gmail.com")
# print("아이디 입력 완료")
# elem = browser.find_element_by_class_name("VfPpkd-dgl2Hf-ppHlrf-sM5MNb")
# print("다음 버튼 찾기 완료")
# elem.click()
# print("다음 버튼 클릭 완료")

# # # 인하대 로그인
# # time.sleep(interval * 2)
# # elem = browser.find_element_by_id("username")
# # elem.send_keys("12161095")
# # elem = browser.find_element_by_id("password")
# # elem.send_keys("tmakdlf!23")
# # elem = browser.find_element_by_id("submit")
# # elem.click()


# # 계속 버튼 클릭
# time.sleep(interval * 2)
# elem = browser.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div")
# elem.click()
# # 로그인

# # 저장
# time.sleep(interval * 2)
# placeLists = list()
# placeLists.append("나사렛국제병원")
# placeLists.append("동춘동 로이드밤")

# for place in placeLists:
#     # 검색창 찾고 쓰기
#     elem = browser.find_element_by_id("searchboxinput")
#     elem.clear()
#     elem.send_keys(place)
#     time.sleep(interval)

#     # 검색 버튼 클릭
#     elem = browser.find_element_by_id("searchbox-searchbutton")
#     elem.click()
#     time.sleep(interval * 2)

#     # [저장] 클릭
#     elem = browser.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[2]/button")
#     elem.click()
    
#     # [별표 표시된 장소] 클릭
#     elem = browser.find_element_by_xpath("//*[@id='action-menu']/ul/li[5]")
#     elem.click()


