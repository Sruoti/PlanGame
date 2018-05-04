from tkinter import *

root = Tk()

theLb = Listbox(root)
theLb.pack()

for item in ['a','b','c','d','e','f','g']:
     theLb.insert(END,item)

theButton = Button(root,text='删除',command=lambda x=theLb:x.delete(ACTIVE))
theButton.pack()

theLb.delete(1)
mainloop()



