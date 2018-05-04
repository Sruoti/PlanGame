class Turtle:

    def _init_(self, name):  #相当于构造函数
        self.name = name

    #属性
    color = 'red'
    weight = 10
    #方法
    def a(self):
        print('这是a')

b = Turtle()
b.a()

class Ball:
    def __init__(self,name='倩倩',age=18):  #构造函数
        self.__name = name
        self.__age = age
    def call(self):
        print('name: %s age: %d'% (self.__name,self.__age))
c = Ball('嘟嘟',20)
c.call()
d = Ball()
d.call()

class chi(Ball):
    #super()
    def __del__(self):
        print('del')
    def __init__(self):
        #Ball.__init__(self,name="嘟嘟2",age=21)  #此处的self是指chi的实例对象
        super.__init__()
        print('null')
    def __init__(self,name,owner):
        self.__name = name
        self.__owner = owner
        self._Ball__name = '嘟嘟3'   #因为父类的call函数，调用的是私有变量
        self._Ball__age = 22
    def __set_name__(self, owner, name):
        self.__name = name
        self.__owner = owner
        print(owner,name)
    def call2(self):
        print('222%s %s' % (self.__name,self.__owner))

v = chi('VV','SS')
v.call()
v.call2()
