#生成器
def myGenerator(x,y,n=10):
    a = x
    b = y
    n = n
    while True:
       a, b = b, a + b
       if a > 100:
           raise StopIteration
       yield a    ##########################

test = myGenerator(0,1)

for each in test:
    print(each , ' ')
    








