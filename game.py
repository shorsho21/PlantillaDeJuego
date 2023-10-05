import pygame
import sys
from config import *
from pygame.locals import *
from scenes import *
from mis_funciones.button import *
from mis_funciones.class_font import *
from mis_funciones.class_image import *
from mis_funciones.class_sound import *
from mis_funciones.class_insert_text import *

class Game:
    def __init__(self) -> None:
        # INICIAMOS EL INIT
        pygame.init()
        # SETEAMOS LOS FPS
        self.clock = pygame.time.Clock()
        # DISPLAY
        self.display = pygame.display.set_mode(SIZE_SCREEN)
        self.display.fill(CUSTOM)
        pygame.display.set_caption("example")

        # FONTS
        self.font = Font("./assets/fonts/HelpMe.ttf", self.display, 30, 40, 50)
        self.name = InsertText(self.display,self.font.font_1,BLANCO)

        # IMAGES
        self.fondo = Image("./assets/images/start_background.jpg",SIZE_SCREEN,self.display,1)

        #sounds
        self.sound_rain = Sound("./assets/sounds/rain_sound.mp3")


        # CONDICIONES DEL JUGO
        self.is_playing = False
        self.is_game_over = False
        self.is_running = False
        self.is_starting = False

    def play(self):
        self.is_playing = False
        self.is_running = True
        self.is_game_over = False
        self.is_pause = False
        self.is_starting = True

        while self.is_starting:
            self.show_start_screen()

        while self.is_running:
            self.clock.tick(FPS)
            self.handler_events()
            self.update()
            self.render()

    def handler_events(self):
        # PARA CERRAR LA VENTANA
        self.close_window()

    def update(self):
        pass

    def render(self):

        if self.is_game_over:
            self.show_game_over_screen()

        elif self.is_playing:

            if self.is_pause:

                pass

        else:
            self.show_start_screen()

        pygame.display.flip()

    def show_start_screen(self):
        """Funcion de la pantalla de inicio
        """
        self.flag_start = True
        while self.flag_start:
            # SETEAMOS EL RELOJ
            self.clock.tick(FPS)
            # pide nombre
            self.name.insert(CENTER)

            #sound
            self.sound_rain.play(-1)
            # seteamos el mensaje
            self.fondo.show(CENTER,True)
            self.font.show_message("Rain man", 2, CENTER, False, NEGRO)
            
            # Input de start y cerrar el juego
            self.input_start_game()
            # flipeo de pantalla
            
            pygame.display.flip()

    def show_game_over_screen(self):
        # TEXTO DE GAME OVER

        pygame.display.flip()
        pygame.time.delay(4000)
        self.is_game_over = False
        self.is_playing = False

    def input_start_game(self):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s or evento.key == 13:
                    self.is_starting = False
                    self.is_playing = True
                    self.flag_start = False
                    # self.is_game_over = True
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def close_window(self):
        """Funcion para poder cerrar la ventana del juego
        """
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT or eventos.type == K_ESCAPE:
                pygame.quit()
                sys.exit()


    
