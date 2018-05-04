from tkinter import *

root = Tk()
menubar = Menu(root)
list1 = []
for i in range(1000):
    list1.append(i)
variable = StringVar()
variable.set(list1[0])
w = OptionMenu(root,variable,*tuple(list1))  #实参解包，形参打包
w.pack()

mainloop()



