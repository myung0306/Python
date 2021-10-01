def print_coin():
    print("비트코인")
print_coin()

for i in range(100):
    print_coin()

def print_coin1():
    for i in range(100):
        print("비트코인")
print_coin1()

def hello():
    print("hello")
hello()

def message():
    print("A")
    print("B")
message()
print("C")
message()

print("a")
def message1():
    print("b")
print("c")
def message2():
    print("d")
message()
print("e")
message1()
#acbed

def message3():
    print("a")
def message4():
    print("b")
    message3()
message4()
#ba

def message5():
    print("a")
def message6():
    print("b")
def message7():
    for i in range(3):
        message6()
        print("c")
    message5()
message7()
#bcbcbca

def 함수(문자열):
    print(문자열)
함수("안녕")
함수("hi")

def 함수(a,b):
    print(a+b)
함수(3, 4)
함수(7, 8)

def print_with_smile(a):
    print(a+":D")
print_with_smile("안녕하세요")

def price_upper_price(price):
    print(price*1.3)
price_upper_price(10)

def price_sum(a, b):
    print(a+b)
price_sum(3, 4)

def print_arithmetic_operation(a, b):
    print("%d + %d = %d" % (a, b, a+b))
    print("%d - %d = %d" % (a, b, a-b))
    print("%d * %d = %d" % (a, b, a*b))
    print("%d / %d = %f" % (a, b, a/b))
print_arithmetic_operation(3, 4)