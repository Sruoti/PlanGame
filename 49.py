from tkinter import *

root = Tk()

text = Text(root,width=30,height=2)  #width为字符的平均高度，2行
text.pack()

text.insert(INSERT,'dudu \n')  #INSERT为输入光标所在的位置
text.insert(END,'棒棒哒')

mainloop()



