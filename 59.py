from tkinter import *

root = Tk()

def callback():
    print("hello world")

mb = Menubutton(root,text='点我',relief=RAISED)
mb.pack()

fileMenu = Menu(mb,tearoff=False)
fileMenu.add_command(label="打开",command=callback)
fileMenu.add_command(label="保存",command=root.quit)
fileMenu.add_separator()
fileMenu.add_command(label="退出",command=root.quit)

mb.config(menu=fileMenu)

mainloop()



