import time
from selenium import webdriver

browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe")

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("basdf")
browser.find_element_by_id("pw").send_keys("password")
# browser.find_element_by_id("id").send_keys("네이버 아이디")
# browser.find_element_by_id("pw").send_keys("비밀번호")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3) # 3초 대기(하지 않으면 전환 시간때문에 입력이 안될 수 있다.)

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()        # 값을 지워주는 역할
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료