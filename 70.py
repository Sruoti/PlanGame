import pygame
import sys

#初始化Pygame
pygame.init()

size = width,height = 500, 300
speed = [-2,1]  #水平方向偏移-2，y偏移1的意思
bg = (255,255,255)

screen_size = pygame.display.list_modes()  #返回数组

clock = pygame.time.Clock()  #控制速度，即帧率

#创建指定大小的窗口,返回Surface 背景画布
screen = pygame.display.set_mode(size,pygame.RESIZABLE)

fullscreen = False
#设置窗口标题
pygame.display.set_caption("hello world")

#加载图片
oturtle = pygame.image.load("E:\\JetBrains\\workspace_2\\project1\\00XX\\006XWZdqgy1fkq1he6gjwj30bm0ewjuj.jpg")
turtle = oturtle

#设置方法缩小的比率
ratio = 1.0

#获得图像的位置矩形
oturtle_rect = turtle.get_rect()
position = turtle_rect = oturtle_rect

#旋转之后的turtle
turtle_right = pygame.transform.rotate(turtle,90)
turtle_top = pygame.transform.rotate(turtle,180)
turtle_left = pygame.transform.rotate(turtle,270)
turtle_bottom = pygame.transform.rotate(turtle,360)

l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turtle = l_head
                speed = [-1,0]
            if event.key == pygame.K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == pygame.K_UP:
                speed = [0, -1]
            if event.key == pygame.K_DOWN:
                speed = [0, 1]
            # 全屏
            if event.key == pygame.K_1:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen_size[0]), pygame.FULLSCREEN | pygame.HWSURFACE)
                    width,height = screen_size  #元祖
                else:
                    screen = pygame.display.set_mode(size)
            #方法。缩小(=、-)，空格键恢复原始尺寸
            if event.key == pygame.K_EQUALS or event.key == pygame.K_MINUS or event.key == pygame.K_SPACE:
                #最大只能方法一倍，缩小50%
                if event.key == pygame.K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == pygame.K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == pygame.K_SPACE:
                    ratio = 1.0
                turtle = pygame.transform.smoothscale(oturtle,(int(oturtle_rect.width * ratio),int(oturtle_rect.height * ratio)))
                l_head = turtle
                r_head = pygame.transform.flip(turtle,True,False)

            #用户调整窗口尺寸
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width,height = size
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    #移动图片
    position = position.move(speed)

    if position.right > width:
        turtle = turtle_right #turtle_right是在初始化定义的，即left生成位置为(0,0)
        position = turtle_rect = turtle.get_rect()#旋转之后矩形改变，
        position.left = width - turtle_rect.width  #矩形只有在最右边才会>width。所以相当于总长减去旋转后矩形的长度。定位在最右边
        speed = [0,1]  #向下
        print("right")
    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width   #定位的是矩形的左上点
        position.top = height - turtle_rect.height
        speed = [-1,0]
        print("bottom")
    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        #position.top = height - turtle_rect.height
        speed = [0, -1]  #向上
        print("left")
    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        #position.left = width - turtle_rect.width
        #position.top = height - turtle_rect.height
        speed = [1, 0]
        print("top")
    #填充背景
    screen.fill(bg)

    #更新图片
    screen.blit(turtle,position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    #pygame.time.delay(10)
    clock.tick(200) #帧率不超过200






