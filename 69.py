import pygame
import sys
import random

#初始化Pygame
pygame.init()
size = width,height = 1000, 600
speed = [-2,1]  #水平方向偏移-2，y偏移1的意思
bg = (0,0,0)
#创建指定大小的窗口,返回Surface 背景画布
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption("hello world")
# 填充背景
screen.fill(bg)
font = pygame.font.Font(None,20)  #字体
#位置：
position = 0
line_height = font.get_linesize()
w = [0,width/2]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position += line_height
        screen.blit(font.render(str(event), True, (0, 255, 0)),(w[random.randint(0,1)],position))
        position += line_height
        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()










