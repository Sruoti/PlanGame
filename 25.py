#迭代器

class Fibs:
    def __init__(self,x,y,n=10):
        self.a = x
        self.b = y
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b, self.a+self.b  #有点6
        if self.a > self.n:
            raise StopIteration
        return self.a

fib = Fibs(1,1)
count = 0
for each in fib:
    if each < 20:
        print('each的值是:%d,次数是: %d' % (each,count))
        count += 1
    else:
        break


    








