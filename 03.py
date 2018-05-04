list1 = [1,2,3,4]
list2 = [2,3,4,5]

for i in list1:
    list2.append(i)

print(list2)

list2 *= 5

print('dudu' in list2)
print('dudu' not in list2)

list1.count(1)

list2.reverse()
print(list2)

list2.sort(reverse=True)
print(list2)