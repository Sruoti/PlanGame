from tkinter import *

class App:
    def __init__(self,master):
        frame = Frame(master)  #框架
        frame.pack(side= LEFT,padx=10,pady=10) #调整位置

        self.hi_there = Button(frame,text='打招呼',fg = 'blue',command = self.sayHi)
        self.hi_there.pack()

    def sayHi(self):
        print('hello world')
root = Tk()


#以不同的颜色区别各个frame
for fm in ['red','blue','yellow','green','white','black']:
    #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
    Frame(height = 20,width = 400,bg = fm).pack()
#向下面的Frame中添加一个Label
#Label(fm[1],text = 'Hello label').pack()
#fm[0].pack()
#fm[1].pack()
root.mainloop()
#Label被添加到下面的Frame中了，而不是root默认的最上方。
#大部分的方法来自gm,留到后面gm时再介绍
root.mainloop()





