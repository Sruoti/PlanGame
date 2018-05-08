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

class Music():
    def __init__(self, music):
        self.music = music
        self.GAMEOVER = USEREVENT

    # 右键开启
    def music_play(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def sound_play(self):
        pygame.mixer.Sound(self.music)
        pygame.mixer.Sound(self.music).set_volume(0.2)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def game_end(self):
        pygame.mixer.music.set_endevent(self.GAMEOVER)

    def music_stop(self):
        pygame.mixer.music.stop()

