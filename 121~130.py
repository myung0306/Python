a = input()
if a.isupper():
    print(a.lower())
else:
    print(a.upper())

score = int(input("score: "))
if score > 80 and score <= 100:
    print("grade is A")
elif score > 60 and score <= 80:
    print("grade is B")
elif score > 40 and score <= 60:
    print("grade is C")
elif score > 20 and score <= 40:
    print("grade is D")
else:
    print("grade is E")

환율 = {"달러": 1167, "엔": 1.069, "유로": 1268, "위안": 171}
won = input("입력: ")
num, currency = won.split()
print(float(num)*환율[currency], "원")

l = []
for i in range(3):
    a = int(input("input num"+str(i+1)+"? "))
    l.append(a)
print(max(l))

num = input("휴대전화 번호 입력: ")
number = num.split("-")
tel = {"011": "SKT", "016": "KT", "019": "KT", "010": "알수없음"}
print("당신은", tel[number[0]], "사용자입니다.")

add = {"0": "강북구", "1": "강북구", "2": "강북구", "3":" 도봉구", "4": "도봉구",
       "5": "도봉구", "6":"노원구", "7":"노원구", "8":"노원구", "9":"노원구"}
add_num = input("우편번호: ")
print(add[add_num[2]])

add_num = input("우편번호: ")
add_num = add_num[:3]
if add_num in ["011", "012", "013"]:
    print("강북구")
elif add_num in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

num = input("주민등록번호: ")
num = num.split("-")[1]
id_num = {"1":"남자", "2":"여자", "3":"남자", "4":"여자"}
print(id_num[num[0]])

str = input().split("-")[1]
if 0 <= int(str[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc["max_price"])-float(btc["min_price"])
시가 = float(btc["opening_price"])
최고가 = float(btc["max_price"])

if 최고가 > (변동폭+시가):
    print("하락장")
else:
    print("상승장")