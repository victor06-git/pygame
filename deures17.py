import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import cuadricula

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (50, 120, 200)



pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # dibuix
    
    
    for angle in range(0, 361, 15):
        pos_x_y = cuadricula.point_on_circle((300,250), 25, angle)
        pos2_x_y = cuadricula.point_on_circle((300,250), 100, angle)

        pos0 = (pos_x_y["x"], pos_x_y["y"])
        pos1 = (pos2_x_y["x"], pos2_x_y["y"])

        pygame.draw.line(screen, BLACK, pos0, pos1, 5)


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()