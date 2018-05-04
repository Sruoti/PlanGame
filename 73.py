import pygame
import sys
from pygame.locals import *
import math

pygame.init()
size = width, height = pygame.display.list_modes()[8]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

points = [(200, 75), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]

lines_points = [(100,10),(150,5),(200,5),(200,70)]

circle_position = size[0] // 2, size[1] // 2

screen = pygame.display.set_mode(size)
pygame.display.set_caption("嘟嘟")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)

    # 绘制矩形
    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)

    pygame.draw.polygon(screen, GREEN, points, 0)

    pygame.draw.circle(screen, RED, circle_position, 25, 1)
    pygame.draw.circle(screen, GREEN, circle_position, 75, 1)
    pygame.draw.circle(screen, BLUE, circle_position, 125, 1)
    circle_position = pygame.mouse.get_pos()

    pygame.draw.ellipse(screen, BLACK, (100, 100, 440, 100), 1)
    pygame.draw.ellipse(screen, BLUE, (220, 50, 200, 200), 1)

    pygame.draw.arc(screen, RED, (0, 0, 200, 200), 0, math.pi / 2, 1)
    pygame.draw.arc(screen, RED, (0, 0, 200, 200), math.pi, math.pi * 3 / 2, 1)

    pygame.draw.lines(screen,BLUE,0,points,2)

    pygame.draw.line(screen,BLACK,(100,200),(540,250),1)

    pygame.draw.aaline(screen, BLACK, (100, 205), (540, 255), 1) #这个1表示开启锯齿

    pygame.draw.aaline(screen, BLACK, (100, 210), (540, 260), 0)  # 这个1表示开启锯齿

    pygame.display.flip()
    clock.tick(10)
