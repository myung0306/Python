#초보자를 위한 파이썬 300제

for i in range(1, 10):
    print("3*%d = %d" % (i, 3*i))
print("\n")
for i in range(1, 10, 2):
    print("3*%d = %d" % (i, 3*i))
print("\n")
sum = 0
for i in range(1, 11):
    sum = i+sum
print(sum)

s = 0
for i in range(1, 11, 2):
    s = i+s
print(s)

s1 = 1
for i in range(1, 10):
    s1 = i*s1
print(s1)

price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

print("\n")

for i in range(len(price_list)):
    print(price_list[i])

print("\n")

for i in range(len(price_list)):
    print("%d %d" % (i, price_list[i]))

print("\n")
for i in enumerate(price_list):
    print(i)

print("\n")
for i in range(len(price_list)):
    print((len(price_list)-1)-i, price_list[i])

print("\n")
for i in range(1, 4):
    print(90+10*i, price_list[i])

print("\n")
my_list = ["가", "나", "다", "라"]
for i in range(1, 4):
    print(my_list[i-1], my_list[i])

print("\n")

my_list = ["가", "나", "다", "라", "마"]
for i in range(3):
    for j in range(3):
        print(my_list[i+j], end="")
    print("\n", end="")

print("\n")
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])

print("\n")
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    for j in range(len(my_list), 2, -1):
        print(my_list[j-1-i], end="")
    print("\n", end="")

print("\n")

my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    sum = 0
    for j in range(3):
        sum = sum + my_list[j+i]
    print("%f \n" % (sum/3), end="")

low_price = [100, 200, 400, 800, 1000]
high_price = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_price)):
    volatility.append(high_price[i]-low_price[i])
print(volatility)
