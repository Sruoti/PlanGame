import pygame
import sys
from pygame.locals import *
import math
from random import *
from tkinter import *
import webbrowser
from tkinter import colorchooser
from planeGame import music
from planeGame import myplane

#增加炸弹的补给箱
class BlueBoom(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(r"E:\JetBrains\image\wsparticle_dafangkuai3.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.width, self.height = bg_size
        self.mask = pygame.mask.from_surface(self.image)  # 检测非透明部分是否碰撞
        self.speed = [randint(-2, 2), randint(1, 2)]
        self.active = False
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), randint(-300, -120)

    def move(self):
        if self.rect.top < self.height:
            self.rect.left += self.speed[0]
            self.rect.top += self.speed[1]
            if self.rect.left < 0 or self.rect.right > self.width:
                self.speed[0] = -self.speed[0]
        else:
            self.active = False
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), randint(-300, -120)

#左下角显示炸弹数目
class BoomVisible():
    def __init__(self,bg_size):
        self.image = pygame.image.load(r"E:\JetBrains\image\wsparticle_64.png").convert()
        self.width,self.height = bg_size
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = \
            10, self.height - 10 - self.rect.height

#改变普通子弹形态的补给箱
class YellowBullet(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"E:\JetBrains\image\wsparticle_dafangkuai1.png").convert()
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size
        self.image.set_colorkey((255, 255, 255))
        self.mask = pygame.mask.from_surface(self.image)  # 检测非透明部分是否碰撞
        self.speed = [randint(-2,2),randint(1,2)]
        self.active = False
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), randint(-300, -200)
    def move(self):
        if self.rect.top < self.height:
            self.rect.left += self.speed[0]
            self.rect.top += self.speed[1]
            if self.rect.left < 0 or self.rect.right > self.width:
                self.speed[0] = -self.speed[0]
        else:
            self.active = False
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), randint(-300, -200)

#将普通子弹换成超级子弹
class RedPackge(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(r"E:\JetBrains\image\wsparticle_dafangkuai2.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.width, self.height = bg_size
        self.mask = pygame.mask.from_surface(self.image)  # 检测非透明部分是否碰撞
        self.speed = [randint(-2, 2), randint(1, 2)]
        self.active = False
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), randint(-130, -120)

    def move(self):
        if self.rect.top < self.height:
            self.rect.left += self.speed[0]
            self.rect.top += self.speed[1]
            if self.rect.left < 0 or self.rect.right > self.width:
                self.speed[0] = -self.speed[0]
        else:
            self.active = False
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), randint(-130, -120)