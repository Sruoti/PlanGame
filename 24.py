class ConList:
    def __init__(self,*args):  #包裹
        self.list1 = [x for x in args] #列表推导式
        self.dict1 = {}.fromkeys(range(len(self.list1)),0)  #这个要好好看，有点6。设置键
    def __len__(self):
        return len(self.list1)
    def __getitem__(self, item):
        self.dict1[item] += 1
        return self.list1[item]








