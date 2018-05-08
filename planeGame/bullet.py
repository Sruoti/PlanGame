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

class Bullet1(pygame.sprite.Sprite):
    bullet_image1 = r"E:\JetBrains\image\wsparticle_27.png"
    bullet_image2 = r"E:\JetBrains\image\wsparticle_68.png"
    bullet_image3 = r"E:\JetBrains\image\wsparticle_dasheng010.png"
    bullet_image4 = r"E:\JetBrains\image\wsparticle_chengsejiguang.png"
    bullet_list = []
    bullet_list.extend([bullet_image1,bullet_image2,bullet_image3,bullet_image4])

    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = Bullet1.bullet_list[0]
        self.image = pygame.image.load(self.bullet_image).convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.image.set_colorkey((255, 255, 255))
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left, self.rect.top = position

#超级子弹
class Bullet2(pygame.sprite.Sprite):
    bullet_image1 = r"E:\JetBrains\image\wsparticle_46.png"
    bullet_image2 = r"E:\JetBrains\image\wsparticle_68.png"
    bullet_image3 = r"E:\JetBrains\image\wsparticle_dasheng010.png"
    bullet_image4 = r"E:\JetBrains\image\wsparticle_chengsejiguang.png"
    bullet_list = []
    bullet_list.extend([bullet_image1, bullet_image2, bullet_image3, bullet_image4])

    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_image = Bullet1.bullet_list[0]
        self.image = pygame.image.load(self.bullet_image).convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.image.set_colorkey((255, 255, 255))
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left, self.rect.top = position


