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
    x1,x2,x3,x4 = 50,100,100,50
    x5 = 75
    for q in range(0, len(colors)):    
        #quadrats
        pygame.draw.polygon(screen, colors[q], [(x1,50),(x2,50),(x3,100),(x4,100)])
        x1  += 100
        x2  += 100
        x3  += 100
        x4  += 100
        #cercles
        pygame.draw.circle(screen, colors[q], (x5,175), 25, 3)
        x5 +=  100
    
    def draw_polygon(screen, color, center, radius, num_vertices, angle_offset=(math.pi / 3)):
        points = [
            (
                center[0] + radius * math.cos(angle_offset + i * 2 * math.pi / num_vertices),
                center[1] + radius * math.sin(angle_offset + i * 2 * math.pi / num_vertices)
            )
            for i in range(num_vertices)
        ]
        pygame.draw.polygon(screen, color, points)
    
    greys = [(0,0,0),(25,25,25),(50,50,50),(75,75,75),(100,100,100),(125,125,125)]
    x6 = 75
    for q in range(0, len(greys)):
        draw_polygon(screen, greys[q], (x6, 275), 25, 3, 1)
        #polygons
        draw_polygon(screen,  greys[q], (x6, 375), 25, 5, 1)
        x6 += 100
        
        







            


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()