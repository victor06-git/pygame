import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import cuadricula
from assets.svgmoji.emojis import get_emoji

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

#Cotxe
path = os.path.join(os.path.dirname(__file__), "./assets/exercici13/car.png")
img_car = pygame.image.load(path).convert_alpha()
img_car = cuadricula.scale_image(pygame, img_car, target_width=15)

#Circuit
path = os.path.join(os.path.dirname(__file__), "./assets/exercici13/circuit.png")
img_circuit = pygame.image.load(path).convert_alpha()
img_circuit = cuadricula.scale_image(pygame, img_circuit, target_height=480)

car = {
    "x": 245,
    "y": 430,
    "angle": 270,
    "speed": 100,
    "img": img_car,
    "direction_x": "none",
    "direction_y": "none",
}
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
   



    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()