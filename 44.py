from tkinter import *

root = Tk()

#单选框

group1 = LabelFrame(root,text="Label框架",padx=5,pady=5)
group1.pack(padx=10,pady=10)
c = IntVar()
Radiobutton(group1,text='one',variable=c,value=1).pack(anchor=W)
Radiobutton(group1,text='TWO',variable=c,value=2).pack(anchor=W)
Radiobutton(group1,text='THREE',variable=c,value=3).pack(anchor=W)
Radiobutton(group1,text='four',variable=c,value=4).pack(anchor=W)

#复选框
group2 = LabelFrame(root,text="Label框架",padx=5,pady=5)
group2.pack(padx=10,pady=10,side=LEFT)
Girls = ['1','2','3','4']
v = []
for girl in Girls:
    v.append(IntVar())
    b = Checkbutton(group2,text=girl,variable=v[-1])
    b.pack()

mainloop()
