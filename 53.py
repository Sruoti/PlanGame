from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5,undo=True,autoseparators=False)
text.pack()

text.insert(END, "I LOVE DUDU")

def callback(event):
    text.edit_separator()  #每当有键输入的时候，插入一个分割符
text.bind("<Key>",callback)


def getIndex(text, pos):
    tuple_1 = tuple(map(int, str.split(text.index(pos), '.')))
    list_1 = list(tuple_1)
    list_2 = [list_1[0],list_1[1]+1]
    tuple_2 = tuple(list_2)
    return tuple_2
start = "1.0"
while True:
    pos = text.search("U", start, stopindex=END)
    if not pos:  #就是if !pos ，但Python中没有这种写法
        break
    print((getIndex(text, pos)))
    start = pos + "+1c"  #"+1c"会自动寻找到下一个字符的位置

def chexiao():
    text.edit_undo()

Button(root,text="撤销",command=chexiao).pack()
mainloop()
