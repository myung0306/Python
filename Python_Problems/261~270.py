#초보자를 위한 파이썬 300제

class human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("응애응애")

    def __del__(self):
        print("나의 죽음을 알리지마라.")

    def who(self): #메소드
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = human("아름", 25, "여자")
print(areum.name, areum.age)
areum.who()
areum.setInfo("불명", "미상", "모름")
areum.who()
del(areum)
class stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

samsung = stock("samsung", "005930")
print(samsung.name, samsung.code)
v = stock(None, None)
v.set_code("005930")
v.set_name("samsung")
print(v.code, v.name)

sk = stock("sk", "005931")
print(sk.name, sk.code)
print(sk.get_name(), sk.get_code())

class stock1():
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_per(self):
        return self.per


samsung = stock1("삼성전자", "005930", "15.79", "1.33", "2.83")
print(samsung.name, samsung.code, samsung.per)
print(samsung.set_name("kt"), samsung.set_code("005860"), samsung.set_per("17.89"))
print(samsung.name, samsung.code, samsung.per)
print(samsung.get_name(), samsung.get_code(), samsung.get_per())

l = []
samsung = stock1("삼성전자", "005930", 15.79, 1.33, 2.83)
lotte = stock1("현대차", "005380", 8.70, 0.35, 4.27)
lg = stock1("LG전자", "066570", 317.34, 0.69, 1.37)

l.append(samsung)
l.append(lotte)
l.append(lg)

for i in l:
    print(i.code, i.per)
