import pygame
from game import *
from config import *
from pygame.locals import *


class Image:
    def __init__(self,path:str,size:tuple,display:pygame.surface.Surface,type_image:int) -> None:
        self.display = display
        if type_image == 1:
            self.image = pygame.image.load(path).convert()
        elif type_image == 2:
            self.image = pygame.image.load(path).convert_alpha()

        
        self.image = pygame.transform.scale(self.image,size)


    def show(self, position, center: bool = False):
        if center:
            self.image_rect = self.image.get_rect()
            self.image_rect.center = position
            self.display.blit(self.image, self.image_rect)

        else:
            self.display.blit(self.image, position)



    
