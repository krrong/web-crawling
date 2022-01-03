import requests
# user agent를 넣어줘서 사용자가 접속한 것을 알려준다.
url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status() # 정상인지 아닌지 바로 확인

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)