import requests
# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
print("응답 코드 : ", res.status_code) # 200이면 정상
res.raise_for_status() # 정상인지 아닌지 바로 확인

# requests.codes.ok == 200
if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
    
print(len(res.text))
print(res.text)