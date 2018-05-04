from tkinter import *
root = Tk()

def callback():
    print('点我')


Label(root,text='textlabel').pack()
Button(root,text='点我',command=callback).place(relx=0.5,rely=0.5,anchor=CENTER)

Label(root,bg='blue').place(relx=0.5,rely=0.5,relheight=0.75,relwidth=0.75,anchor=CENTER)
Label(root,bg='red').place(relx=0.5,rely=0.5,relheight=0.5,relwidth=0.5,anchor=CENTER)
Label(root,bg='yellow').place(relx=0.5,rely=0.5,relheight=0.25,relwidth=0.25,anchor=CENTER)
Button(root,text='点我',command=callback).place(relx=0.5,rely=0.5,anchor=CENTER)
mainloop()




