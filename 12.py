dict2 = {}
dict2 = dict2.fromkeys((range(3)),'number')
print(dict2)
for i in dict2:
    print(i,' ',dict2[i])
for j in dict2.values():
    print(j)
for k in dict2.items():
    print(k)

print(dict2.get(5))
print(dict2.get(5,5))
print(dict2.get(2,'木有'))

for m in dict2.items():
    print(m)
print(6 not in dict2)
