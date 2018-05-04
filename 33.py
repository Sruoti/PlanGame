import re

str1 = 'src="http://www.cc900.cn/wp-content/uploads/2017/09/cc900.cn_2017-09-15_19-35-42.jpg'
list1 = str1.split('/',4)

a = str1.split('/')[-1]
print(a)

list2 = str1.split('=')
print(len(list1))
print(list1)

regex = 'img class="" src=[^"]+\.jpg' #[^"]要注意点
result = re.search(r"(\w+)  (\w+)","duud  dudu  udud")
#print(result)
rg = result.group()
#print(result.group(2))
#print(result.start(1))

