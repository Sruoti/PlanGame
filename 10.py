def a():
    print("hello world")

def func1():
    x = 10
    def func2():
        nonlocal x
        x *= x
        return x
    return func2()
print(func1())

def funcX(x):
    def funcY(y):
        return x*y
    return funcY
print(funcX(5)(8))

b = lambda x,y : x * y + 1
print(b(2,3))

print(list(filter(lambda x : x % 2, range(10))))
print(list(map(lambda x : x * 2, range(10))))
