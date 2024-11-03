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
GREY = (200,200,200)


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
    
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # dibuix
    y1,y2,y3,y4 = 50,50,100,100 
    color = 0
    for row in range(8):
        x1,x2,x3,x4 = 50,100,100,50  
        for column in range(8): 

            if color  == 0:
                color1 = GREY
            elif color == 1:
                color1 =  BLACK  

            pygame.draw.polygon(screen, color1, [(x1,y1),(x2,y2),(x3,y3),(x4,y4)])
            x1 += 50 
            x2 += 50
            x3 += 50
            x4 += 50
            color = (color  + 1) % 2
        y1  +=  50
        y2  +=  50
        y3  +=  50
        y4  +=  50
        color = (color  + 1) % 2




            


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()