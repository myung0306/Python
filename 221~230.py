def n_plus_1(n):
    result = n + 1
    return result

print(n_plus_1(3))

def make_url(url):
    return url

print(make_url("www.naver.com"))

def make_list(l):
    a = []
    for i in l:
        a.append(i)
    return a
print(make_list("abcd"))

def pickup_even(l):
    return l[1::2]
print(pickup_even([3, 4, 5, 6, 7, 8]))

def convert_int(n):
    return int(n.replace(",", ""))

print(convert_int("1,234,567"))

def fun(n):
    return n + 4
a = fun(10)
b = fun(a)
c = fun(b)
print(c)

def fun1(n):
    return n + 5
d = fun1(fun1(fun1(10)))
print(d)

def fun2(n):
    return n + 4
def fun3(n):
    return n * 10
a = fun2(10)
c = fun3(a)
print(a, c)

def test(n):
    return n + 4
def test1(n):
    n = n + 2
    return test(n)

c = test1(10)
print(c)

def test2(n):
    return n * 2
def test3(n):
    return test2(n + 2)
def test4(n):
    n = n + 10
    return test3(n)

c = test4(2)
print(c)
