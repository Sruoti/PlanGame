import pickle
list1 = [1,2,3,4,5,6]
pickle_file = open('C:\\Users\\ZHJ\\Desktop\\test.txt','wb')
pickle.dump(list1,pickle_file)     #将列表存储到pickle_file中
pickle_file.close()


pickle_file2 = open('C:\\Users\\ZHJ\\Desktop\\test.txt','rb')
list2 = pickle.load(pickle_file2)
print(list2)
pickle_file2.close()
