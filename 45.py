from tkinter import *

class App():
    def __init__(self):
        self.root = Tk()
        #self.frame = LabelFrame(root,padx=10,pady=10)
        #self.frame.pack(padx=10,pady=10)
    def ifTrue(self):
        self.text = Label(self.root, text='输入正确')  ###
        self.text.grid(row=0,column=1,sticky=W,padx=10, pady=10)
        mainloop()
    def ifFalse(self):
        self.text = Label(self.root, text='输入错误')
        self.text.grid(row=2,column=1,sticky=W,padx=10, pady=10)
        mainloop()

def showTrue():
    app = App()
    app.root.title('showTrue')
    app.ifTrue()

def showFalse():
    app = App()
    app.root.title('showFalse')
    app.ifFalse()

#####################################################3

def test(content,reason,name):
   if content == '小甲鱼':
       print(content, reason, name)
       showTrue()
       return True
   else:
       e1.delete(0,END)
       showFalse()
       return False

def test2():
    print('test2')
# 输入框
root = Tk()

Label(root,text='作品').grid(row=0, column=1)
Label(root,text='作者').grid(row=2, column=1)

v1 = StringVar()     #v1,v2的作用是标识
v2 = StringVar()

testCMD = root.register(test)
e1 = Entry(root,textvariable=v1,show="*",validate="focusout",\
           validatecommand=(testCMD,'%P','%v','%W'),invalidcommand=test2)
e1.grid(row=0,column=2,padx=10,pady=5)
e2 = Entry(root,textvariable=v2,show="&")
e2.grid(row=2,column=2,padx=10,pady=5)



def show():
    Label(root, text="作品:《%s》" % e1.get()).grid(row=6,column=1,sticky=W,padx=10,pady=5)
    Label(root, text="作者:  %s" % e2.get()).grid(row=8, column=1, sticky=W,padx=10, pady=5)


Button(root,text='获取信息',width=10,command=show)\
    .grid(row=4,column=1,sticky=W,padx=10,pady=5)
Button(root,text='退出',width=10,command=root.quit)\
    .grid(row=4,column=2,sticky=E,padx=10,pady=5)

mainloop()




