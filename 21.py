class Rectangle:
    def __init__(self,w=0,h=0):
        self.w = w
        self.h = h

    def __setattr__(self, key, value):
        if key == 's':
            self.w = value
            self.h = value
        else:
            #self.key = value    #  会重复self.w=value.然后触发__setattr__方法.两种解决办法
            super().__setattr__(key,value)
            self.__dict__[key] = value
    def getArr(self):
        return self.h * self.w

r = Rectangle()
print(r.w)
r.h
