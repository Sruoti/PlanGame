from tkinter.filedialog import askopenfilename
fname = askopenfilename(filetypes=(("Template files", "*.tplate"), ("HTML files", "*.html;*.htm")))
answer = '好帅哦'
#input("测试一下Input")
for i in range(2,10,2):
    if answer == input("请输入正确答案"):
        break
    else:
        print(i)
        print("continue之前")
        continue
        print("continue之后")




