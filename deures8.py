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
YELLOW =  (255,255,0)


pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True    
    # Centre de la pantalla
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
    colors = [(127, 184, 68), (240, 187, 64), (226, 137, 50), (202, 73, 65), (135, 65, 152), (75, 154, 217)]
    board = [
    [0, 1, 2, 3, 4, 5, 4, 3],
    [1, 2, 3, 4, 5, 4, 3, 2],
    [2, 3, 4, 5, 4, 3, 2, 1],
    [3, 4, 5, 4, 3, 2, 1, 0],
    [4, 5, 4, 3, 2, 1, 0, 1],
    [5, 4, 3, 2, 1, 0, 1, 2],
    [4, 3, 2, 1, 0, 1, 2, 3],
    [3, 2, 1, 0, 1, 2, 3, 4],
]
    y1,y2,y3,y4 = 50,50,100,100
    for j in range(0,8):
        x1,x2,x3,x4 = 50,100,100,50
        for i in range(0,8):
            pygame.draw.polygon(screen, colors[board[j][i]], [(x1, y1),(x2,y2),(x3,y3),(x4,y4)])
            x1 += 50
            x2 += 50
            x3 += 50
            x4 += 50
        y1 += 50
        y2 += 50
        y3 += 50
        y4 += 50
        


            


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()