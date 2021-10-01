def print_coin():
    for i in range(1, 101):
        print(i, "비트코인")
print_coin()

def message():
    print("A")
    print("B")
message()
print("C")
message()

print("A")

def message1():
    print("B")

print("C")
message1()

print("hello")
def message2():
    print("world")
print("hello1")
def message3():
    print("world1")
message2()
print("hello2")
message3()

def test1():
    print("test1")
def test2():
    print("test2")
def test3():
    for i in range(3):
        test2()
        print("test3")
    test1()
test3()