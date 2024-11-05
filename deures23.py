#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import cuadricula

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  

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

    # Dibuixar la graella
    cuadricula.draw_grid(pygame, screen, 50)

    # Imatge
    # Carregar la imatge
    # Carregar la imatge d'en Shinnosuke
    path_shinnosuke = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shinnosuke.png")
    im_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
    im_shinnosuke = cuadricula.scale_image(pygame, im_shinnosuke, target_width=100)
    # Carregar la imatge d'en Shinnosuke
    path_shiro = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shiro.png")
    im_shiro = pygame.image.load(path_shiro).convert_alpha()
    im_shiro = cuadricula.scale_image(pygame, im_shiro, target_width=75)
    screen.blit(im_shiro, (225, 205))
    screen.blit(im_shinnosuke, (325, 160))
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()