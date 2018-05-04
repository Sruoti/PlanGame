import pygame
import sys

# 初始化Pygame
pygame.init()

size = width, height = 500, 300

bg = (255, 255, 255)



clock = pygame.time.Clock()  # 控制速度，即帧率

# 创建指定大小的窗口,返回Surface 背景画布
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

fullscreen = False

# 设置窗口标题
pygame.display.set_caption("hello world")

# 加载图片
#带alpha通道的Surface不能调用set_alpha()方法
oturtle = pygame.image.load("E:\\JetBrains\\workspace_2\\project1\\00XX\\006XWZdqgy1fkq1he6gjwj30bm0ewjuj.jpg").convert_alpha()
turtle = oturtle

background = pygame.image.load("E:\\JetBrains\\workspace_2\\project1\\00XX\\006XWZdqgy1fl9wj8i761j30j60cs0x7.jpg").convert()

# 获得图像的位置矩形
oturtle_rect = turtle.get_rect()
position = turtle_rect = oturtle_rect

#turtle.set_colorkey((255,255,255))
turtle.set_alpha(200)

#一个一个的修改透明度
# for i in range(position.width):
#     for j in range(position.height):
#         temp = turtle.get_at((i,j))  #获得点的像素值
#         if temp[3] != 0:  # R,G,B,A A表示透明度
#             temp[3] = 200
#         turtle.set_at((i,j),temp)


def blit_aplha(target,source,location,opacity):  #screen,turtle
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(),source.get_height())).convert() #获得矩形区域
    temp.blit(target,(-x,-y))  ##绘制背景，相当于小乌龟对应的背景区域
    temp.blit(source,(0,0))    #带alpha通道的小乌龟图片贴上去
    temp.set_alpha(opacity)
    target.blit(temp,location)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 用户调整尺寸
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            position.center = width//2,height//2

    screen.blit(background, (0, 0))

    blit_aplha(screen,turtle,position,200)

    # 填充背景
   # screen.fill(bg)

    # 更新图片
    # screen.blit(background, (0,0))
    # screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    # pygame.time.delay(10)
    clock.tick(200)  # 帧率不超过200
