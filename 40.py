import tkinter as tk

class App():
    def __init__(self,master):
        frame = tk.Frame(master,bg='red')  #框架
        frame.pack(side= tk.LEFT,padx=10,pady=10) #调整位置

        self.hi_there = tk.Button(frame,text='打招呼',fg = 'blue',command = self.sayHi)
        self.hi_there.pack()

        textLabel = tk.Label(master, text="lebel2")
        textLabel.pack(side=tk.LEFT)

        #photo = tk.PhotoImage(file="E:\JetBrains\workspace_2\project1\00XX\006KR5vWgy1fjjylho38qj30j60asdjb.jpg")
        #tk.Label(master,image=photo)

    def sayHi(self):
        print('hello world')

root = tk.Tk()
app = App(root)
root.mainloop()





