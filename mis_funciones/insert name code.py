import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ingresar Nombre")

# Configuración de fuentes
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

def main():
    user_name = ""
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Si se presiona ENTER, aquí podrías utilizar el nombre ingresado
                    # en la variable `user_name` para lo que necesites.
                    print("Nombre ingresado:", user_name)
                    user_name = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Si se presiona BACKSPACE, borramos el último carácter del nombre
                    user_name = user_name[:-1]
                else:
                    # Agregar el carácter ingresado al nombre
                    user_name += event.unicode

        # Limpiar la pantalla
        window.fill((0, 0, 0))

        # Dibujar el nombre en pantalla
        text_surface = font.render("Nombre: " + user_name, True, text_color)
        window.blit(text_surface, (20, 20))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de la ventana
        clock.tick(60)

if __name__ == "__main__":
    main()
