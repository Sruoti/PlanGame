import sys
print(sys.path)
def c2f(cel):
    return cel*1.8+32
def f2c(fah):
    return (fah-32)/1.8

def test():
    print('摄氏0：华氏：',c2f(0))
    print('华氏0：摄氏：',f2c(0))

if __name__ == '__main__':   #因为这是测试语句，所以，不希望被导入的时候调用。27.py 被导入的时候，在其他文件中__name__ = 27
    test()






