import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

newses = soup.find_all("div", attrs={"class":"cjs_t"})
links = soup.find_all("a", attrs={"class":"cjs_news_a"})

for link in links:
    print(link["href"])

for idx, news in enumerate(newses):
    print(news.get_text())
    print(" ▶ 링크 주소 : " + links[idx]["href"])
    

    