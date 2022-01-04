import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # excel 파일에서 한글이 깨지면 utf8 -> utf-8-sig로 바꿔주자
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", "전일비" ...]
writer.writerow(title)

for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        
        # 의미 없는 데이터는 skip
        if len(columns) <= 1: 
            continue
        
        # 불필요한 공백 삭제
        data = [column.get_text().strip() for column in columns]
        # print(data)
        
        # 데이터는 list형태로 넣어줘야 한다.
        writer.writerow(data)