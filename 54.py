from tkinter import *
import hashlib
from math import *
root = Tk()

w = Canvas(root,width=600,height=200,background="white")
w.pack()

line1 = w.create_line(0,50,200,50,fill="yellow")
line2 = w.create_line(100,0,100,100,fill="red",dash=(4,4))  #虚线
rect1 = w.create_rectangle(50,25,150,75,fill="blue")
w.create_oval(40,20,160,80,fill="green")#椭圆
w.create_text(100,50,text="嘟嘟")  #文本
w.create_arc(-10,-10,100,100)  #弧形
center_x = 100
center_y = 50
r = 50
points = [
    center_x - int(r * sin(2* pi /5)),center_y - int(r * cos(2*pi/5)),#左上点
    center_x + int(r * sin(2* pi /5)),center_y - int(r * cos(2*pi/5)),#右上点
    center_x - int(r * sin(pi /5)),center_y + int(r * cos(pi/5)),#左下点
    center_x,center_y - r,#顶点
    center_x + int(r * sin(pi /5)),center_y + int(r * cos(pi/5)),#右下点
    ]
w.create_polygon(points,outline="red",fill="red")  #多边形

# w.coords(line1,100,0,0,100)  #移动
# w.itemconfig(rect1,fill="pink")  #换颜色
# w.delete(line2) #删除

mainloop()
