import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import cuadricula
import random

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 
PINK = (255,105,180)


pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    global center_x, center_y
    is_looping = True    
    # Centre de la pantalla
    center_x, center_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
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
    #Centre pantalla
    center_x, center_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # dibuix
    x,y = center_x, center_y
    pixels = 15
    direccio = 0

    
    
    for _ in range (25):   
        if direccio == 0:
            coord_x, coord_y = x + pixels, y
        elif direccio == 1:
            coord_x, coord_y = x - pixels, y
        elif  direccio == 2:
            coord_x, coord_y = x, y + pixels
        elif  direccio == 3:
            coord_x, coord_y = x, y - pixels

        pygame.draw.line(screen, RED,(x,y), (coord_x,coord_y), 5)

        x,y = coord_x, coord_y
        direccio = (direccio + 1) % 4
        pixels += 15


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()