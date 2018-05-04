from tkinter import *
def callback():
    var.set('solve has change')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("demo")
textLabel = Label(frame1,
                  text=var,
                  justify=LEFT,
                  padx=0)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="E:\JetBrains\workspace_2\project1\00XX\006KR5vWgy1fjjylho38qj30j60asdjb.jpg")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="solve", command=callback)
theButton.pack()

frame1.pack(pdx=10)
frame2.pack(pdx=10)

mainloop()
