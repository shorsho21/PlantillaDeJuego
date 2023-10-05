import pygame
import sys
from pygame.locals import *
from config import *
class InsertText:
    def __init__(self, display:pygame.surface, font:pygame.font,color:tuple) -> None:
        self.name = ""
        self.display = display
        self.font = font
        self.color = color
        self.clock = pygame.time.Clock()
        self.flag = True
        self.name_inserted = ""

    def insert(self, position):
        
        while self.flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Si se presiona ENTER, aquí podrías utilizar el nombre ingresado
                        # en la variable `user_name` para lo que necesites.
                        print("Nombre ingresado:", self.name)
                        self.name_inserted = self.name
                        self.name = ""
                        self.flag = False
                    elif event.key == pygame.K_BACKSPACE:
                        # Si se presiona BACKSPACE, borramos el último carácter del nombre
                        self.name = self.name[:-1]
                    else:
                        # Agregar el carácter ingresado al nombre
                        self.name += event.unicode

            self.display.fill((0,0,0))
            text_surface = self.font.render("name  " + self.name, True, self.color)
            text_surface_rect = text_surface.get_rect()
            text_surface_rect.center = position
            self.display.blit(text_surface, text_surface_rect)
            
            pygame.display.flip()
            self.clock.tick(60)

            
