from tkinter import *

root = Tk()

Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=200).pack()
Scale(root,from_=0,to=200,length=600,tickinterval=10,resolution=5,orient=HORIZONTAL).pack()




mainloop()



