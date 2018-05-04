from tkinter import *
import hashlib
from math import *
root = Tk()
root.title('绘图')
w = Canvas(root,width=600,height=200,background="white")
w.pack()

paint_color = 'black'

i = 0

def changeColor(color='black'):
    paint_color.replace("black",color)
    print(paint_color)

colorFrame = LabelFrame(root,text="颜色",padx=5,pady=5)
colorFrame.pack(side=LEFT)
redLabel = Label(colorFrame,text="red：",background="red").grid(row=0,column=0,padx=2,pady=2)
br = Button(colorFrame,text="红色",command=changeColor('red'),background="red")
br.grid(row=0,column=2,padx=2,pady=2)
blueLabel = Label(colorFrame,text="blue",background="blue").grid(row=2,column=0,padx=2,pady=2)
Button(colorFrame,text="蓝色",command=changeColor('blue'),background="blue").grid(row=2,column=2,padx=2,pady=2)
yellowLabel = Label(colorFrame,text="yellow",background="yellow").grid(row=4,column=0,padx=2,pady=2)
Button(colorFrame,text="黄色",command=changeColor('yellow'),background="yellow").grid(row=4,column=2,padx=2,pady=2)

def paint(event):
    x1,y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill= paint_color)
w.bind("<B1-Motion>",paint)  #与鼠标左键绑定
Label(root,text="绘画出自己的艺术吧").pack()

Button(root,text="清屏",command=(lambda x=ALL:w.delete(x))).pack(side=BOTTOM,padx=5,pady=19)

mainloop()
