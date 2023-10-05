import pygame
from game import *
from config import *
from pygame.locals import *


class Button:
    def __init__(self, font: pygame.font.Font, message: str = "example", color: tuple = BLANCO, position: tuple = CENTER) -> None:
        self.font = font
        self.text = self.font.render(message, True, color)
        self.position = position
        self.sound = pygame.mixer.Sound("./assets/sounds/buttom_fx.wav")
        self.massage = message
        self.color = color
        self.flag = True
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.position
        self.sound_word = pygame.mixer.Sound("./assets/sounds/BBS Menu.wav")
        self.sound_word.set_volume(0.50)

    def show_button(self, display: pygame.surface.Surface):

        display.blit(self.text, self.text_rect)

    def mostrar_texto_animado(self, display, retraso=100):
        if self.flag:
            for i in range(len(self.massage) + 1):
                if self.flag:  # Limpia la pantalla con color negro
                    texto_mostrar = self.font.render(
                        self.massage[:i], True, self.color)  # Renderiza el texto parcial
                    # Muestra el texto renderizado
                    display.blit(texto_mostrar, self.text_rect)
                    pygame.display.flip()
                    pygame.time.delay(retraso)
                    self.sound_word.play()  # Pequeño retraso entre letras
        self.flag = False

        if self.flag == False:
            texto_mostrar = self.font.render(
                self.massage, True, self.color)  # Renderiza el texto parcial
            display.blit(texto_mostrar, self.text_rect)
            pygame.time.delay(retraso)
