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
PINK = (255,105,180)


pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')
dir_x = 'none'
pos_x = 100
radio = 25

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
    global dir_x

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dir_x = 'right'
            elif event.type == pygame.K_LEFT:
                dir_x =  'left'
        elif  event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if  dir_x == 'right':
                    dir_x = 'none'
            elif event.key == pygame.K_LEFT:
                if   dir_x == 'left':
                    dir_x = 'none'

    return True

# Fer càlculs
def app_run():
    global dir_x, pos_x, radio

    delta_time = clock.get_time()/1000.0

    speed = 100
    displacement = speed * delta_time
    width = screen.get_width() - radio
    
    if (dir_x == "right"):
        pos_x = pos_x + displacement
        if (pos_x > width):
            pos_x = width
    elif (dir_x == "left"):
        pos_x = pos_x - displacement
        if (pos_x < radio):
            pos_x = radio
    radio = 10 + (pos_x / 8)




# Dibuixar
def app_draw():
    global pos_x
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    font = pygame.font.SysFont("Arial", 24)
    text = font.render('Apreta les tecles (left/right)', True, BLACK)
    screen.blit(text, (50, 50))
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # dibuix
    
    pygame.draw.circle(screen, BLACK,  (pos_x, 250), radio)

    

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()