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
    dreta = x + pixels
    esquerre = x - pixels
    amunt = y + pixels
    avall = y - pixels
    x,y = center_x, center_y
    pixels = 15
    direccio = dreta
    if direccio == dreta:
        coord_x, coord_y = dreta, y
    elif direccio == esquerre:
        coord_x, coord_y = esquerre, y
    elif  direccio == amunt:
        coord_x, coord_y = x, amunt
    elif  direccio == avall:
        coord_x, coord_y = x, avall


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()