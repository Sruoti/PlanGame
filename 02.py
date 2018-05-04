array = [1,2,3,'嘟嘟','qianqian']

array.append("棒棒哒")
array.insert(0,"insert")

print(array)
print(array[1:4])

del array[1]
print(array.pop(3))
print(array.remove(2))
print(array)

b = array[:]
print(b)