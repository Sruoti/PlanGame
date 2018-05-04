import pygame
import sys

# 初始化Pygame
pygame.init()

size = width, height = 500, 300
speed = [-2, 1]  # 水平方向偏移-2，y偏移1的意思
bg = (255, 255, 255)

screen_size = pygame.display.list_modes()  # 返回屏幕大小数组

clock = pygame.time.Clock()  # 控制速度，即帧率

# 创建指定大小的窗口,返回Surface 背景画布
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

fullscreen = False
# 设置窗口标题
pygame.display.set_caption("hello world")

# 加载图片
oturtle = pygame.image.load("E:\\JetBrains\\workspace_2\\project1\\00XX\\006XWZdqgy1fkq1he6gjwj30bm0ewjuj.jpg")
turtle = oturtle

# turtle = pygame.transform.chop(oturtle,(207,200,50,50)) #裁剪图片 207.200为裁剪中心点。

# 设置方法缩小的比率
ratio = 1.0

# 获得图像的位置矩形
oturtle_rect = turtle.get_rect()
position = turtle_rect = oturtle_rect

#position.center = width // 2, height // 2

# 0->未选择,1->选择中， 2->完成选择
select = 0
select_rect = pygame.Rect(0, 0, 0, 0)
# 0->未拖拽，1->拖拽中,2->完成拖拽
drag = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # 用户调整窗口尺寸

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 第一次点击选择范围
                if select == 0 and drag == 0:
                    pos_start = event.pos
                    select = 1
                # 第二次点击，拖拽图像
                elif select == 2 and drag == 0:
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()
                    drag = 1
                # 第三次点击，初始化
                elif select == 2 and drag == 2:
                    select = 0
                    drag = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # 第一次释放
                if select == 1 and drag == 0:
                    pos_stop = event.pos
                    select = 2
                # 第二次释放,结束拖拽
                if select == 2 and drag == 1:
                    drag = 2

        # 用户调整尺寸
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # 实时绘制选择框
    if select:
        mouse_pos = pygame.mouse.get_pos()
        if select == 1:
            pos_stop = mouse_pos
        select_rect.left, select_rect.top = pos_start
        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
        pygame.draw.rect(screen,(0,0,0),select_rect,1)  #将矩形画到屏幕上
        test_rect = pygame.Rect(10,10,10,10)
        test_rect.center = width // 2, height // 2
        pygame.draw.rect(screen, (0, 0, 0), test_rect, 1)
        print("执行到这里")

    # 拖拽裁剪的图像
    if drag:
        if drag == 1:
            cap_rect.center = mouse_pos
        screen.blit(capture,cap_rect)
    # 填充背景
    screen.fill(bg)

    # 更新图片
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    # pygame.time.delay(10)
    clock.tick(200)  # 帧率不超过200
