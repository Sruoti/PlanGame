import pygame
import sys

#初始化Pygame
pygame.init()

size = width,height = 1000, 600
speed = [-2,1]  #水平方向偏移-2，y偏移1的意思
bg = (255,255,255)

clock = pygame.time.Clock()  #控制速度，即帧率

#创建指定大小的窗口,返回Surface 背景画布
screen = pygame.display.set_mode(size)

#设置窗口标题
pygame.display.set_caption("hello world")

#加载图片
turtle = pygame.image.load("E:\\JetBrains\\workspace_2\\project1\\00XX\\006XWZdqgy1fkq1he6gjwj30bm0ewjuj.jpg")

#获得图像的位置矩形
position = turtle.get_rect()
f = open("E:\\JetBrains\\workspace_2\\project1\\record.txt",'w')
while True:
    for event in pygame.event.get():
        f.write(str(event)+"\n")
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()
    #移动图片
    position = position.move(speed)

    if position.left < 0 or  position.right > width:
        #翻转图片
        turtle = pygame.transform.flip(turtle,True,True)#水平翻转，垂直翻转
        #反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    #填充背景
    screen.fill(bg)

    #更新图片
    screen.blit(turtle,position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    #pygame.time.delay(10)
    clock.tick(200) #帧率不超过200






