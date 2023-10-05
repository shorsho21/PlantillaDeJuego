import pygame
from game import *
from config import *
from pygame.locals import *

class Sound:
    def __init__(self,path:str,volume:float = 1) -> None:
        self.sound = pygame.mixer.Sound(path)
        self.sound.set_volume(volume)
        self.flag = True
        

    def play(self,loop: int = 0, flag : bool = True):
        if flag:
            if self.flag:
                self.sound.play(loop)
                self.flag = False
        elif flag == False:
                self.sound.play(loop)
                self.flag = False

    def stop(self):
        self.sound.stop()
        