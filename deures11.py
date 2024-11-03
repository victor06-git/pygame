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
    global dir_x, dir_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_UP:
                dir_y = 'up'
            elif  event.key == pygame.K_DOWN:
                dir_y = 'down'
            elif   event.key == pygame.K_LEFT:
                dir_x = 'left'
            elif   event.key == pygame.K_RIGHT:
                dir_x = 'right'
        elif  event.type == pygame.KEYUP:
            if  event.key == pygame.K_UP:
                if dir_y == 'up':
                    dir_y = 'none'
            elif   event.key == pygame.K_DOWN:
                if dir_y == 'down':
                    dir_y ='none'
            elif    event.key == pygame.K_LEFT:
                if  dir_x == 'left':
                    dir_x = 'none'
            elif     event.key == pygame.K_RIGHT:
                if  dir_x == 'right':
                    dir_x = 'none'
    return True

# Fer càlculs
def app_run():
    global dir_x, dir_y, pos_x, pos_y

    delta_time = clock.get_time()/1000.0

    speed = 50
    displacement = speed * delta_time

    if (dir_x == "right"):
        pos_x = pos_x + displacement
        if (pos_x > 450):
            pos_x = 450
    elif (dir_x ==  "left"):
        pos_x = pos_x - displacement
        if (pos_x < 0):
            pos_x = 0
    elif  (dir_y == "down"):
        pos_y = pos_y - displacement
        if (pos_y > 450):
            pos_y = 450
    elif (dir_y == "up"):
        pos_y = pos_y + displacement
        if (pos_y < 0):
            pos_y = 0




# Dibuixar
def app_draw():
    global pos_x, pos_y
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # dibuix
    radio = 10 + (pos_x / 8)
    pygame.draw.circle(screen, BLACK,  (int(pos_x), int(pos_y)), radio)

    

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()