from selenium import webdriver

# 크롬창을 띄우지 않고 백그라운드로 동작
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

browser = webdriver.Chrome("./webscraping_basic/chromedriver.exe", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# 실제 user agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/96.0.4664.110 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

# headless chrome으로 접속했을 때 user agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# HeadlessChrome/96.0.4664.110 Safari/537.36
browser.quit()