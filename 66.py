from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

root = Tk()

def callback():
    filename = filedialog.askopenfilename(
        filetypes=[("PNG","png"),("GIF","gif"),("All","*")],  #（类型名，后缀名）默认的文件类型
        defaultextension=".png")    #自动添加后缀
    print(filename)

def chosecolor():
    color = colorchooser.askcolor()  #看颜色的RPG值
    print(color)

Button(root,text='打开文件',command=callback).pack()
Button(root,text='选择颜色',command=chosecolor).pack()
mainloop()





