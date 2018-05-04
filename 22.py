class MyDesc:
    def __get__(self, instance, owner):
        print('getting...',self,instance,owner)
    def __set__(self, instance, value):
        print('setting...', instance, value)
    def __delete__(self, instance):
        print('deleting...', instance)

class Test:
    x = MyDesc()

t = Test()
t.x
t.x = '嘟嘟'
del t.x