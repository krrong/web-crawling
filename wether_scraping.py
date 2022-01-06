import requests
from bs4 import BeautifulSoup

location = input("날씨를 알고싶은 동을 입력하세요 : ")
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + location + "날씨"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print("-"*100)
print("오늘 " + location + "의 날씨 입니다!")


# 현재 온도, 어제와 비교한 날씨 출력
temperature = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
summary_today = soup.find("p", attrs={"class":"summary"}).get_text().strip().split()
summary = summary_today[0] + " " + summary_today[1] + " " + summary_today[2]
print(temperature + " " + summary_today[3] + "(" + summary +")")

# 미세먼지, 초미세먼지, 자외선, 일몰시각 출력
today_chars = soup.find("ul", attrs={"class":"today_chart_list"}).find_all("li")
for today_char in today_chars:
    print(today_char.get_text().strip())

# 오늘 날씨 시간순으로 출력
low_temperature = 100
high_temperature = -100
hourly_weathers = soup.find("div", attrs={"class":"graph_inner _hourly_weather"}).find_all("li")

for hourly_weather in hourly_weathers:
    hourly_weather_list = hourly_weather.get_text().split()
    # 오늘까지만 출력
    if hourly_weather_list[0] == "내일":
        break
    
    print(hourly_weather.get_text().strip())
    
    # tmp에 온도만 저장
    tmp = ""
    for i in hourly_weather_list[2]:
        if i == "°":
            break
        tmp = tmp + i
    
    # string 을 int로 변환
    tmp = int(tmp)
    
    # 오늘 최저기온 갱신
    if low_temperature > tmp:
        low_temperature = tmp

    # 오늘 최대기온 갱신
    if high_temperature < tmp:
        high_temperature = tmp

print("최저 기온 : ", low_temperature)
print("최대 기온 : ", high_temperature)


# 강수 확률 출력
summary_list = soup.find("dl", attrs={"class":"summary_list"}).find("dd")
print("강수 확률 : " + summary_list.get_text())

print("-"*100)