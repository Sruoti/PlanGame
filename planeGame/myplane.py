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


class Plane(pygame.sprite.Sprite):
    def __init__(self, image1, image2, image3, image4, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image_up = pygame.image.load(image4).convert()
        self.image_right = pygame.image.load(image2).convert()
        self.image_left = pygame.image.load(image3).convert()
        self.image_down = pygame.image.load(image1).convert()
        list_image = [self.image_up, self.image_right, self.image_left, self.image_down]
        for i in list_image:
            i.set_colorkey((255, 255, 255))
            # i.set_alpha(200)

        self.rect = self.image_up.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, (self.height - self.rect.height - 20)
        self.speed = 10
        self.boom_num = 3
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image_up) #检测非透明部分是否碰撞

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua2.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua1.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua3.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_guanyu91.png").convert()
        ])
        for j in self.destroy_images:
            j.set_colorkey((255, 255, 255))
            j.set_alpha(200)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 20:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 20

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.left < self.width - self.rect.width:
            self.rect.left += self.speed
        else:
            self.rect.left = self.width - self.rect.width

    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, (self.height - self.rect.height - 20)
        self.active = True
        self.invincible = True