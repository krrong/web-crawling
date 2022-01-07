import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

interval = 3
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
url = "https://cu.bgfretail.com/event/plus.do?category=event"
browser.get(url)

# 1+1 버튼 클릭
time.sleep(interval)
elem = browser.find_element_by_class_name("eventInfo").find_element_by_link_text("1+1").click()
time.sleep(interval)

while True:
    time.sleep(interval)
    # 더보기 버튼 받아오기
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='contents']/div[1]/div[2]/div/div[1]/a")))
    
    # 더보기 버튼이 없으면 종료
    if not elem:
        break
    
    # 더보기 버튼 클릭
    elem.click()


# 2+1 버튼 클릭
elem = browser.find_element_by_class_name("eventInfo").find_element_by_link_text("2+1").click()
time.sleep(interval)
interval = 15
while True:
    time.sleep(interval)
    # 더보기 버튼 받아오기
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='contents']/div[1]/div[2]/div/div[1]/a")))
    
    # 더보기 버튼이 없으면 종료
    if not elem:
        break
    
    # 더보기 버튼 클릭
    elem.click()
