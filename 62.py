from tkinter import *

root = Tk()

w = Message(root,text='DUDU',width=100).pack()

Spinbox(root,from_=0,to=100,wrap=True,values=("小甲鱼","陈都灵")).pack()   #wrao开启循环

m1 = PanedWindow(showhandle=True,sashrelief=SUNKEN)
m1.pack(fill=BOTH,expand=1)
m1.add( Label(m1,text="left pane"))
m2 = PanedWindow(showhandle=True,sashrelief=SUNKEN,orient=VERTICAL)
m1.add(m2)
m2.add(Label(m2,text="top"))
m2.add(Label(m2,text="bottom"))


def create():
    top = Toplevel()
    top.attributes("-alpha",0.5)  #设置透明度
    top.title("Fishc.com")
    Message(top,text="I LOVE FISHC").pack()

Button(root,text="创建顶级窗口",command=create).pack()

mainloop()



