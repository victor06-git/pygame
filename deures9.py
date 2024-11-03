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
BLUE  = (50, 120, 200)
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
    # dibuix text  
    dades = [ 
  {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
  {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
  {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
  {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
  {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
  {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'} ]
    #Fons blancs
    fons = (255, 255, 255)
    pygame.draw.rect(screen, fons, (150, 100, 200, 150))
    #Linias negras
    y1,y2 = 100,100
    for _ in range (7):
        pygame.draw.line(screen, BLACK,  (150,y1), (350, y2), 4)
        y1 += 25
        y2 += 25
    #Text
    for i in range(0,  len(dades)):

        font = pygame.font.SysFont("Arial", 18)
        font2 =  pygame.font.SysFont("Arial", 16)
        text = font.render(dades[i]['nom'], True, BLACK)
        text2 = font2.render(str(dades[i]['any']), True, BLUE)
        text3 = font2.render(str(dades[i]['especie']), True, BLUE)
        y3 =  102 + (i * 25)
        screen.blit(text, (155,y3))
        screen.blit(text2, (255,y3))
        screen.blit(text3, (305,y3))


    


        


            


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()