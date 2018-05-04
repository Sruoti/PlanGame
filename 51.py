from tkinter import *
import webbrowser
root = Tk()

text = Text(root,width=30,height=10)
text.pack()

text.insert(INSERT,"I LOVE DUDU,ALTHOUGH ....")
text.tag_add("tag1","1.7","1.12","1.15")
text.tag_add("tag2","1.7","1.12","1.15")
text.tag_config("tag1",background="yellow",foreground="red")
text.tag_config("tag2",foreground="blue") #会覆盖

def show_hand_cursor(event):
    text.config(cursor="arrow")
def show_xterm_cursor(event):
    text.config(cursor="xterm")
def click(event):
    webbrowser.open("http://www.baidu.com")
text.tag_add("link","1.0","1.4")
text.tag_config("link",foreground="green",underline=True)

text.tag_bind("link","<Enter>",show_hand_cursor)  #链接绑定
text.tag_bind("link","<Leave>",show_xterm_cursor)
text.tag_bind("link","<Button-1>",click)

text.tag_lower("tag2") #tag之间的优先级

text.insert(END+"\n","DUDU DUDU",("tag2","tag1"))
mainloop()



