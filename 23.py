class Celsius:
    def __init__(self,value=0):
        self.value = float(value)
        print('摄氏%d度' % self.value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:   #华氏
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value) -32) /1.8


class Temeperature:
  #  def __init__(self, value = 30):
   #     self.cel = value
    cel = Celsius()
    fah = Fahrenheit()

temp = Temeperature()
temp.cel = 20
print(temp.cel,temp.fah)