dict1 = {}
dict1 = dict1.fromkeys((range(10)),'嘟嘟')
for i in dict1.items():
    print('i:',i)

dict2 = dict1.copy()  #浅拷贝。更改dict2。对dict1没有任何影响
for j in dict2.items():
    print('j:',j)

dict1.popitem()  #随机弹出来一个数据。从字典中删除
print(dict1)

a = {"小白":'狗'}
dict1.update(a)
print(dict1)