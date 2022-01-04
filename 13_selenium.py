# pip install selenium==3.141.0
from selenium import webdriver

# ()안에 chromedriver.exe의 경로를 넣어주어야 함
browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")
browser.get("http://naver.com")

# 로그인 버튼 찾기
elem = browser.find_elements_by_class_name("link_login")
elem

# 로그인 버튼 클릭
elem.click()

# browser.back()      # 뒤로가기
# browser.forward()   # 앞으로가기
# browser.refresh()   # 새로고침

# 검색창 찾기
elem = browser.find_element_by_id("query")
elem

# ENTER키 입력을 위한 import
from selenium.webdriver.common.keys import Keys
elem.send_keys("검색할 단어")
elem.send_keys(Keys.ENTER)

# tag name으로 찾기
elem = browser.find_element_by_tag_name("a")
elem

# 다음으로 이동
browser.get("http://daum.net")

# 검색창 찾기
elem = browser.find_element_by_name("q")
elem

# 단어 입력 및 Enter
elem.send_keys("검색할 단어")
elem.send_keys(Keys.ENTER)

# xpath를 이용하여 검색하기
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem
elem.click()

# 브라우저 한 개 종료(현재 탭 종료)
browser.close()

# 브라우저 전체를 종료(여러 탭 동시 종료)
browser.quit()