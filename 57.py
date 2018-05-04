from tkinter import *

root = Tk()

def callback():
    print("hello")

menubar = Menu(root)

def callback():
    print("hello world")

menubar.add_command(label="撤销",command=callback)
menubar.add_command(label="重做",command=callback)

root.config(menu=menubar)

mainloop()



