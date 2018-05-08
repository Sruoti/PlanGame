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


class SmallEnemy(pygame.sprite.Sprite):
    energy = 2
    def __init__(self, image_red, image_yellow, image_green, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image_red = pygame.image.load(image_red).convert()
        self.image_yellow = pygame.image.load(image_yellow).convert()
        self.image_green = pygame.image.load(image_green).convert()
        self.image_list = [self.image_red, self.image_yellow, self.image_green]
        for i in self.image_list:
            i.set_colorkey((255, 255, 255))
            # i.set_alpha(200)
        self.width, self.height = bg_size
        self.rect = self.image_red.get_rect()
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-self.height, 0)
        self.speed = 1
        self.active = True
        self.energy = SmallEnemy.energy
        self.mask = pygame.mask.from_surface(self.image_red)
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua2.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua1.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua3.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_guanyu91.png").convert()
        ])
        for j in self.destroy_images:
            j.set_colorkey((255, 255, 255))
            #j.set_alpha(200)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = SmallEnemy.energy
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    energy = 4
    def __init__(self, image, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((255, 255, 255))
        # self.image.set_alpha(200)
        self.width, self.height = bg_size
        self.rect = self.image.get_rect()
        self.rect.left = randint(0, self.width - self.rect.width) #0, self.width - self.rect.width
        self.rect.top = randint(-10 * self.height, -self.height)  # -10 * self.height, -self.height
        self.speed = 1
        self.active = True
        self.energy = MidEnemy.energy
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua2.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua1.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua3.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_guanyu91.png").convert()
        ])
        for j in self.destroy_images:
            j.set_colorkey((255, 255, 255))
            #j.set_alpha(200)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-15 * self.height, -5 * self.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self, image, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        # self.image.set_alpha(200)
        self.width, self.height = bg_size
        self.rect = self.image.get_rect()
        self.rect.left = randint(0, self.width - self.rect.width)  #0, self.width - self.rect.width
        self.rect.top = randint(-10 * self.height, -5 * self.height)  #-10 * self.height, -5 * self.height
        self.speed = 1
        self.active = True
        self.energy = BigEnemy.energy
        self.mask = pygame.mask.from_surface(self.image)
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua2.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua1.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_chongwufuhua3.png").convert(),
            pygame.image.load(r"E:\JetBrains\image\wsparticle_guanyu91.png").convert()
        ])
        for j in self.destroy_images:
            j.set_colorkey((255, 255, 255))
            #j.set_alpha(200)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-10 * self.height, -5 * self.height)
