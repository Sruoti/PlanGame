import pygame
import sys
from pygame.locals import *
import math
from random import *
import io
from pydub import AudioSegment
import wave
from tkinter import *
import webbrowser
from tkinter import colorchooser

circle_d = 30


class Music():
    def __init__(self, music, sound):
        self.music = music
        self.sound = sound
        self.GAMEOVER = USEREVENT

    # 右键开启
    def music_play(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()

    def sound_play(self):
        pygame.mixer.Sound(self.sound)
        pygame.mixer.Sound(self.sound).set_volume(0.2)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def game_end(self):
        pygame.mixer.music.set_endevent(self.GAMEOVER)

    def music_stop(self):
        pygame.mixer.music.stop()


class Ball(pygame.sprite.Sprite):  # 继承动画精灵基类
    def __init__(self, image, position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.rect.width, self.rect.height = (circle_d, circle_d)
        self.side = [choice([-1, 1]), choice([-1, 1])]  # 水平方向，竖直方向
        self.collide = False
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
        self.radio = 15
        self.target = target
        self.control = False

    # self.image_new = pygame.transform.chop(self.image, (self.rect.left + 15, self.rect.top + 15, 15, 15))

    def move(self):
        # 如果是玩家控制
        if self.control:
            self.rect = self.rect.move(self.speed)
        # 如果是自行移动
        else:
            self.rect = self.rect.move(self.speed[0] * self.side[0],
                                       self.speed[1] * self.side[1])

        if self.rect.right < 0:
            self.rect.left = self.width
        elif self.rect.left > self.width:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0

    def check(self, motion):
        if self.target < motion < self.target * 2:
            return True
        else:
            return False


class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.glass_image = pygame.image.load(glass_image)
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = \
            (bg_size[0] - self.glass_rect.width) // 2, \
            (bg_size[1] - self.glass_rect.height) // 2  # 即放在中心区域

        self.glass_chop_image = pygame.transform.chop(self.glass_image, (bg_size[0] // 2,
                                                                         bg_size[1] // 2,
                                                                         50,
                                                                         50))  # 裁剪图片 207.200为裁剪中心点。

        self.glass_chop_image.set_alpha(0)
        self.glass_chop_image.set_colorkey((255, 255, 255))

        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = \
            self.glass_rect.top, self.glass_rect.top
        self.mouse_rect.width, self.mouse_rect.height = 10, 10
        pygame.mouse.set_visible(False)

    def position_zone(self):
        if self.mouse_rect.left < self.glass_rect.left:
            self.mouse_rect.left = self.glass_rect.left
        if self.mouse_rect.left > self.glass_rect.right - self.mouse_rect.width:
            self.mouse_rect.left = self.glass_rect.right - self.mouse_rect.width
        if self.mouse_rect.top < self.glass_rect.top:
            self.mouse_rect.left = self.glass_rect.left
        if self.mouse_rect.bottom > self.glass_rect.bottom:
            self.mouse_rect.bottom = self.glass_rect.bottom


# 碰撞检测《有现成的pygame.sprite.spritecollide(ball,group,False):》
def collide_check(item, target):
    col_balls = []
    for each in target:
        distance = math.sqrt(
            math.pow((item.rect.center[0] - each.rect.center[0]), 2) +
            math.pow((item.rect.center[1] - each.rect.center[1]), 2))
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)
    return col_balls


def mp3Towav(file):
    with open(file, 'rb') as fp:
        data = fp.read()
    # 主要部分
    aud = io.BytesIO(data)
    sound = AudioSegment.from_file(aud, format='mp3')
    raw_data = sound._data
    # 写入到文件，验证结果是否正确。
    l = len(raw_data)
    f = wave.open(r'C:/Users/ZHJ/Music/b.wav', 'wb')
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(16000)
    f.setnframes(l)
    f.writeframes(raw_data)
    f.close()


def GameEndMessage():
    root = Tk()
    # frame = Frame(root,bg="red",height=200).grid(row=0,column=0)
    Label(root, text='*** GAME WILL STOP RUN *** \n *** thanks your play ***', bg='yellow', fg='blue').grid(row=0,column=0,padx=5,pady=5)
    labelframe = LabelFrame(root, text='**单选复选框**',padx=5, pady=5)
    labelframe.grid(row=2, column=0, padx=5, pady=5)
    Label(labelframe, text='这个游戏您有什么评价吗?', bg="pink").grid(row=6, column=0, padx=5, pady=5)
    v = IntVar()
    Radiobutton(labelframe, text='太好完了', padx=5, pady=5, variable=v, value=1).grid(row=7, column=0, padx=5,pady=5)
    Radiobutton(labelframe, text='一般', padx=5, pady=5, variable=v, value=2).grid(row=8, column=0, padx=5,pady=5)
    Radiobutton(labelframe, text='差评', padx=5, pady=5, variable=v, value=3).grid(row=9, column=0, padx=5,pady=5)
    Checkbutton(labelframe, text="复选框1", padx=5, pady=5, variable=IntVar()).grid(row=7, column=3, padx=5,
                                                                                          pady=5)
    Checkbutton(labelframe, text="复选框2", padx=5, pady=5, variable=IntVar()).grid(row=8, column=3, padx=5,
                                                                                          pady=5)
    Checkbutton(labelframe, text="复选框3", padx=5, pady=5, variable=IntVar()).grid(row=9, column=3, padx=5,
                                                                                          pady=5)
    #e1 = Entry(root, textvariable=v1, show="*", validate="focusout", validatecommand=(testCMD, '%P', '%v', '%W'), invalidcommand=test2)
    Label(labelframe,text="您的姓名:").grid(row=10,column=0,padx=5,pady=5)
    Entry(labelframe,textvariable=StringVar()).grid(row=10,column=3,padx=5,pady=5)
    Label(labelframe, text="您的联系方式:").grid(row=11, column=0, padx=5, pady=5)
    Entry(labelframe, textvariable=StringVar()).grid(row=11, column=3, padx=5, pady=5)
    sb = Scrollbar(root)

    listbox = Listbox(labelframe,yscrollcommand=sb.set)
    listbox.insert(END,"感谢以下开发人员: \n")
    for i in range(1000):
        listbox.insert(END,i)
    listbox.grid(row=12, column=0, padx=5, pady=5,sticky=W)
    sb.grid(row=12, column=0, padx=5, pady=5, sticky=E)   #grid设置滚动条
    sb.config(command=listbox.yview)

    Scale(labelframe, from_=0, to=42, tickinterval=5, resolution=5, length=200).grid(row=12, column=2, padx=5, pady=5)
    #Scale(labelframe, from_=0, to=200, length=600, tickinterval=10, resolution=5, orient=HORIZONTAL).grid(row=12, column=2, padx=5, pady=5)

    # Text()组件
    root.focus_set() #绑定<Key>时必须先设置
    frame = Frame(root)
    frame.grid(row=0,column=4,padx=5,pady=5)
    text = Text(frame,bg='pink',width=30, height=5,undo=True,autoseparators=False)
    text.grid(row=1,column=4,padx=5,pady=5)
    text.insert(INSERT,"这是text组件\n")
    text.insert(END,"姑凉，你的小鼻子皱的很可爱哦~")
    text.tag_add("link",'1.0','1.7')
    text.tag_config("link",background=('green'),foreground="red",underline=True)
    def open(event):
        webbrowser.open("http://www.baidu.com")
    text.tag_bind("link","<Button-1>",open)
    def callback(event):
        text.edit_separator()  # 每当有键输入的时候，插入一个分割符
    text.bind("<Key>", callback)
    def roback():
        text.edit_undo()
    Button(frame,text="撤销",padx=5,pady=5,command=roback).grid(row=1,column=4,padx=5,pady=5,sticky=CENTER and S)
    Label(frame,text='请输入您查找的字符:').grid(row=2,column=4,padx=5,pady=5,sticky=N)
    text_query = Text(frame,width=30, height=5)
    text_query.grid(row=3,column=4,padx=5,pady=5,sticky=S)
    text_visible = Text(frame,width=30, height=2)
    text_visible.grid(row=4,column=4,padx=5,pady=5,sticky=S)
    text_visible.insert(INSERT,"dudu ")
    def getIndex(text, pos):
        list_1 = list(tuple(map(int, str.split(text.index(pos), '.'))))
        tuple_2 = tuple([list_1[0], list_1[1] + 1])
        return tuple_2

    def queryZiFu():
        query_start = "1.0"
        while True:
            pos = text.search(str(text_query.get("1.0",END)),query_start, stopindex=END)
            print(text_query.get("1.0",END))
            if not pos:  # 就是if !pos ，但Python中没有这种写法
                break
            text_visible.insert(END,str(getIndex(text, pos)))
            query_start = pos + "+1c"  # "+1c"会自动寻找到下一个字符的位置
    Button(frame, text="查找", padx=5, pady=5, command=queryZiFu).grid(row=3, column=4, padx=5, pady=5,sticky=CENTER and S)

    #菜单
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=False)
    fileMenu.add_command(label="打开", command=root.quit)
    fileMenu.add_command(label="保存", command=root.quit)
    fileMenu.add_separator()
    fileMenu.add_command(label="退出", command=root.quit)
    menubar.add_cascade(label="文件", menu=fileMenu)

    editMenu = Menu(menubar, tearoff=False)
    editMenu.add_command(label="剪切", command=callback)
    editMenu.add_command(label="拷贝", command=callback)
    editMenu.add_command(label="黏贴", command=callback)
    menubar.add_cascade(label="编辑", menu=editMenu)

    checkMenu = Menu(menubar, tearoff=False)
    checkMenu.add_checkbutton(label="搜索", command=callback, variable=1)
    checkMenu.add_checkbutton(label="检查", command=callback, variable=2)
    checkMenu.add_checkbutton(label="退出", command=callback, variable=3)
    checkMenu_next = Menu(checkMenu,tearoff=False)
    checkMenu_next.add_checkbutton(label="搜索2", command=callback, variable=1)
    checkMenu_next.add_checkbutton(label="检查2", command=callback, variable=2)
    checkMenu.add_cascade(label="多选文件菜单next",menu=checkMenu_next)
    menubar.add_cascade(label="多选文件菜单", menu=checkMenu)

    editvar = IntVar()
    RadioMenu = Menu(menubar, tearoff=False)
    RadioMenu.add_radiobutton(label="搜索", command=callback, variable=editvar, value=1)
    RadioMenu.add_radiobutton(label="检查", command=callback, variable=editvar, value=2)
    RadioMenu.add_radiobutton(label="退出", command=callback, variable=editvar, value=3)
    menubar.add_cascade(label="单选文件菜单", menu=RadioMenu)

    menubar.add_command(label="撤销",command=callback)

    def popup(event):  # 右键弹出
        menubar.post(event.x_root, event.y_root)
    frame.bind("<Button-3>", popup)
    root.config(menu=menubar)

    frame_2 = LabelFrame(root,text='嘟嘟')
    frame_2.grid(row=5,column=4,padx=5,pady=5)
    Label(frame_2, bg='blue',text='label——1').place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
    Label(frame_2, bg='red',text='label——2').place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
    Label(frame_2, bg='yellow',text='label——3').place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)

    def chosecolor():
        color = colorchooser.askcolor()  # 看颜色的RPG值
        print(color)
    Button(frame_2, text='选择颜色', command=chosecolor).grid(row=5,column=4,padx=5, pady=5,sticky=CENTER and S)

    mainloop()


def main():
    pygame.init()
    pygame.mixer.init()

    running = True

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    PINK = (255.99609375, 0.0, 255.99609375)
    COLOR = [BLACK, GREEN, RED, BLUE, PINK]

    ball_image = "C:\\Users\\ZHJ\\Pictures\\Saved Pictures\\63957_1466095_610157.jpg"
    bg_image = "E:\\JetBrains\\workspace_2\\project1\\00XX\\006XWZdqgy1fltocpnnw4j30hs0bnn23.jpg"
    glass_iamge = r'E:\JetBrains\workspace_2\project1\00XX\006XWZdqgy1fmwz99tklej30j60asdjq.jpg'
    mouse_image = r'E:\JetBrains\workspace_2\project1\00XX\006XWZdqgy1fmwzaex216j30j60y2wo6.jpg'
    bg_size = width, height = pygame.display.list_modes()[8]
    # bg_size = width, height = (800,600)
    screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
    background = pygame.image.load(bg_image).convert_alpha()
    pygame.display.set_caption("嘟嘟")
    clock = pygame.time.Clock()
    balls = []
    holes = [(117, 119, 119, 201), (225, 227, 390, 392),
             (503, 505, 320, 322), (698, 700, 192, 194), (906, 908, 419, 421)]

    group = pygame.sprite.Group()

    # 生成5个小球
    Ball_Num = 10
    for i in range(Ball_Num):
        position = randint(0, width - circle_d), randint(0, height - circle_d)
        speed = [randint(1, 10), randint(1, 10)]
        ball = Ball(ball_image, position, speed, bg_size, 2 * (i + 1))  # 刚开始错误是因为我的ball_image很大，矩形一直碰撞

        # while collide_check(ball, balls):
        #     ball.rect.left, ball.rect.top = randint(0, width - 30), randint(0, height - 30)
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - circle_d), randint(0, height - circle_d)
        balls.append(ball)
        group.add(ball)

    glass = Glass(glass_iamge, mouse_image, bg_size)

    # 1秒内事件发生的次数，与target比较。根据check来判断小球是否停下
    motion = 0
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000)  # 没隔1秒触发

    # 音乐的参数初始化
    music_file = r'C:\Users\ZHJ\Music\a.mp3'
    sound_file = r'C:\Users\ZHJ\Music\b.mp3'
    # mp3Towav(sound_file)  #需要安装ffmpeg
    # sound_file_wav = r'C:\Users\ZHJ\Music\b.wav'
    mus = Music(music_file, sound_file)
    pause_key = False
    mus.game_end()

    pygame.key.set_repeat(100, 1)
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mus.sound_play()  # 不能运行，需要wav格式文件
                if event.button == 3:
                    mus.music_play()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause_key = not pause_key
            if event.type == mus.GAMEOVER:
                pygame.time.delay(2000)
                running = False

            if event.type == MYTIMER:  # 每隔1秒触发，触发后清零
                if motion:
                    for each in balls:  # 每一个小球传入的target不一样。所以是全部小球循环。但check比较的target是不一样的
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True

                    motion = 0
            if event.type == MOUSEMOTION:
                motion += 1

            if event.type == KEYDOWN:
                for each in group:
                    if each.control:
                        if event.key == K_w:
                            each.speed[1] -= 10
                        if event.key == K_s:
                            each.speed[1] += 10
                        if event.key == K_a:
                            each.speed[0] -= 10
                        if event.key == K_d:
                            each.speed[0] += 10

                    if event.key == K_SPACE:
                        if each.control:
                            for hole in holes:
                                if hole[0] < each.rect.left < hole[1] and hole[2] < each.rect.top < hole[3]:
                                    each.speed = [0, 0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(temp)
                                    holes.remove(hole)
                            if not holes:
                                mus.music_stop()
                                pygame.time.delay(300)
                                GameEndMessage()
                                pygame.time.delay(300)
                                pygame.quit()
                                sys.exit()

            # 用户调整尺寸
            elif event.type == pygame.VIDEORESIZE:
                bg_size = event.size
                width, height = bg_size[0], bg_size[1]
                screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)

        if pause_key:
            mus.pause()
        else:
            mus.unpause()

        screen.blit(background, (0, 0))
        screen.blit(glass.glass_chop_image, glass.glass_rect)
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        glass.position_zone()
        screen.blit(glass.mouse_image, glass.mouse_rect)

        for each in group:
            each.move()  # 刚开始是生成-10~10的随即数，有可能生成的随机数还是相撞的方向，所以改为速度始终为正，相撞后，各自的方向取反。
            # 然后相撞后重新生成新的速度
            # screen.blit(each.image, each.rect)  # 加载小球图片到屏幕上
            if each.collide:
                each.speed = [randint(1, 10), randint(1, 10)]
                each.collide = False
            if each.control:
                # pygame.draw.circle(screen, ((randint(0, 255)), (randint(0, 255)), (randint(0, 255))),
                #                    (each.rect.left, each.rect.top),
                #                    circle_d,
                #                    10)
                pygame.draw.rect(screen, ((randint(0, 255)), (randint(0, 255)), (randint(0, 255))),
                                 each.rect,
                                 10)
            else:
                pygame.draw.circle(screen, ((randint(0, 255)), (randint(0, 255)), (randint(0, 255))),
                                   (each.rect.left, each.rect.top),
                                   circle_d,
                                   10)  # 我试试画个圆形
        # 小球碰撞检测，即小球的矩形碰撞检测
        for each in group:
            group.remove(each)
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.side[0], each.side[1] = -each.side[0], -each.side[1]
                each.collide = True
                if each.control:  # 玩家控制的时候速度带方向(即带有正负）
                    each.side[0] = -1  # 从右向左为负，反方向乘以负数为正。从左向右为正，反方向乘以负数为负
                    each.side[1] = -1
                if each.speed[0]:
                    each.control = False
            group.add(each)

        # for i in range(Ball_Num):
        #     item = balls.pop(i)
        #     if collide_check(item, balls):  # 只要检测col_balls中是否含有参数，即是否有发生碰撞<铭记这种思想>
        #         item.speed[0] = -item.speed[0]
        #         item.speed[1] = -item.speed[1]
        #     balls.insert(i, item)

        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
