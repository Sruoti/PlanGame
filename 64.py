from tkinter import *
root = Tk()
root.title('TAT')
Label(root,text='用户名').grid(row=0,sticky=W)
Entry(root).grid(row=0,column=1)
Entry(root,show="*").grid(row=1,column=1)
Label(root,image=PhotoImage(file='')).grid(row=0,column=2)



mainloop()




