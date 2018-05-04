import re

f = open("C:\\Users\\ZHJ\\Desktop\\test.txt", encoding='gb18030', errors='ignore')

boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        # 我们这里进行字符串分割操作
        if re.match('小甲鱼:', each_line) != None:
            (role, line_spoken) = each_line.split(":", 1)  # 切割后保存1，即line_spoken
            if role == '小甲鱼':
                boy.append(line_spoken)
        if re.match('小客服', each_line) != None:
            (role, line_spoken) = each_line.split(":", 1)
            if role == '小客服':
                girl.append(line_spoken)
        print(boy)
        print(girl)

    else:
        # 文件的分别保存
        file_name_boy = 'C:\\Users\\ZHJ\\Desktop\\boy_' + str(count) + ".txt"
        file_name_girl = 'C:\\Users\\ZHJ\\Desktop\\girl' + str(count) + ".txt"
        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1
f.close()
