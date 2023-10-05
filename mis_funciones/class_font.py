import pygame
from config import *
from pygame.locals import *


class Font:
    def __init__(self, path: str, display, size_1: int, size_2: int, size_3: int) -> None:
        self.font_1 = pygame.font.Font(path, size_1)
        self.font_2 = pygame.font.Font(path, size_2)
        self.font_3 = pygame.font.Font(path, size_3)
        self.display = display

    def show_message(self, message: str,font_size : int, position: tuple, antialias: bool = True, color: tuple = (255, 255, 255)):
        if font_size == 1:
            text = self.font_1.render(message, antialias, color)
            text_rect = text.get_rect()
            text_rect.center = position
            self.display.blit(text, text_rect)

        elif font_size == 2:
            text = self.font_2.render(message, antialias, color)
            text_rect = text.get_rect()
            text_rect.center = position
            self.display.blit(text, text_rect)

        elif font_size == 3:
            text = self.font_3.render(message, antialias, color)
            text_rect = text.get_rect()
            text_rect.center = position
            self.display.blit(text, text_rect)
