from tkinter import *

root = Tk()

# sb = Scrollbar(root)
# sb.pack(side=RIGHT,fill=Y)
#
# lb = Listbox(root,yscrollcommand=sb.set)


text = Text(root,width=100,height=10)
text.pack()
text.insert(INSERT,'dudu \n')  #INSERT为输入光标所在的位置
text.insert(END,'棒棒哒')


photo = PhotoImage(file='')

def show():
    text.insert(INSERT,'\n我被点了一下')
    text.image_create(INSERT,image=photo)

b1 = Button(text,text="点我点我",command=show)
text.window_create(INSERT,window=b1)


# lb.pack(side=LEFT,fill=BOTH)
# sb.config(command=lb.yview)

mainloop()



