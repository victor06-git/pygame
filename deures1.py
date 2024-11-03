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
    pygame.draw.rect(screen, RED, (50, 50, 550, 100))
    font = pygame.font.SysFont("Arial", 60)
    text0 = font.render('HEADLINE NEWS', True, WHITE,)
    screen.blit(text0, (75, 70))

    font2 =  pygame.font.SysFont("Courier New", 40, True)
    text1 = font2.render('World goes Wrong!',  True, BLACK)
    screen.blit(text1, (50, 160))

    font3 = pygame.font.SysFont("Arial", 28)
    text2 = font3.render("Lorem ipsum dolor sit amet, consectetur", True, BLACK)
    screen.blit(text2, (50, 250))

    text3 = font3.render("adipiscing elit, sed do eiusmod tempor", True, BLACK)
    screen.blit(text3, (50, 285))

    text4 = font3.render("incididunt ut labore et dolore magna aliqua.", True, BLACK)
    screen.blit(text4, (50, 320))

    text5 = font2.render("YEP#", True, GREEN)
    screen.blit(text5, (510, 150))



    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()