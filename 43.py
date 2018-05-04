from tkinter import *

root = Tk()

v = IntVar()
c = Checkbutton(root,text='测试一下',variable=v)  #复选框?勾选框
c.pack()

l = Label(root,textvariable=v)
l.pack()

mainloop()
