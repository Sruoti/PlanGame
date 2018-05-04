import time
class MyTimer:

    def __init__(self):
        self.prompt = ''
        self.end = 0
        self.begin = 0
        self.last = []

    def __str__(self):
       return self.prompt

    __repr__ = __str__  #直接调用实例类 t  就会找到repr魔法方法

    def __add__(self, other):  #self,other皆为实例化对象
        desc = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.last[index] + other.last[index])
            if result:
                desc += (str(result[index]))
        return desc

    #开始计时
    def start(self):
        self.begin = time.localtime()
        print('计时开始')

    #计时结束
    def stop(self):
        self.end = time.localtime()
        self.__calc()
        print('计时结束')

    #内部方法，计算运行时间
    def __calc(self):
        self.prompt = '总共运行了'
        for index in range(6):
            self.last.append(self.end[index] - self.begin[index])
            self.prompt += str(self.last[index])+'时间'
      #  print(self.prompt)



t1 = MyTimer()
t1.start()
t1.stop()

t2 = MyTimer()
t2.start()
t2.stop()

t1 + t2
