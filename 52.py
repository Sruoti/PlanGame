from tkinter import *
import hashlib
root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(END,"I LOVE DUDU")
contents = text.get("1.0",END)

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents_md5_check = text.get("1.0",END)
    if sig != getSig(contents_md5_check):
        print("酱爆~内容变动")
    else:
        print(sig)
        print("毛事没有")

Button(root,text="检查",command=check).pack()

mainloop()




