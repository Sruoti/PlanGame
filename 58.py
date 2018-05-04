from tkinter import *

root = Tk()

def callback():
    print("hello")

menubar = Menu(root)

def callback():
    print("hello world")

menubar.add_command(label="撤销",command=callback)
menubar.add_command(label="重做",command=callback)

frame = Frame(root,width=512,height=512)
frame.pack()

def popup(event):   #右键弹出
    menubar.post(event.x_root,event.y_root)

frame.bind("<Button-3>",popup)

mainloop()



