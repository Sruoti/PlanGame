from tkinter import *

root = Tk()

def callback(event):
    print("点击位置: %d %d" %(event.x,event.y))

def callchar(event):
    print("按下的键: %s" % event.char)

def callMotion(event):
    print("motion:", event)  #鼠标移动获取焦点事件

frame = Frame(root,width=200,height=200)
frame.pack()
frame.focus_set()  #绑定<Key>时必须先设置
frame.bind("<Button-1>",callback)
frame.bind("<Key>",callchar)
frame.bind("<Motion>",callMotion)

mainloop()



