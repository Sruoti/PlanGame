from tkinter import *

root = Tk()

def callback():
    print("hello world")

menubar = Menu(root)

fileMenu = Menu(menubar,tearoff=False)
fileMenu.add_command(label="打开",command=callback)
fileMenu.add_command(label="保存",command=root.quit)
fileMenu.add_separator()
fileMenu.add_command(label="退出",command=root.quit)
menubar.add_cascade(label="文件",menu=fileMenu)

editMenu = Menu(menubar,tearoff=False)
editMenu.add_command(label="剪切",command=callback)
editMenu.add_command(label="拷贝",command=callback)
editMenu.add_command(label="黏贴",command=callback)
menubar.add_cascade(label="编辑",menu=editMenu)


openvar = IntVar()
savevar = IntVar()
quitvar = IntVar()
checkMenu = Menu(menubar,tearoff=False)
checkMenu.add_checkbutton(label="搜索",command=callback,variable=1)
checkMenu.add_checkbutton(label="检查",command=callback,variable=2)
checkMenu.add_checkbutton(label="退出",command=callback,variable=3)
menubar.add_cascade(label="check",menu=checkMenu)

editvar  = IntVar()
RadioMenu = Menu(menubar,tearoff=False)
RadioMenu.add_radiobutton(label="搜索",command=callback,variable=editvar,value=1)
RadioMenu.add_radiobutton(label="检查",command=callback,variable=editvar,value=2)
RadioMenu.add_radiobutton(label="退出",command=callback,variable=editvar,value=3)
menubar.add_cascade(label="check2",menu=RadioMenu)

root.config(menu=menubar)

mainloop()



