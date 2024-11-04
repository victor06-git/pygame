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


pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

#Cotxe
path = os.path.join(os.path.dirname(__file__), "./assets/exercici013/car.png")
img_car = pygame.image.load(path).convert_alpha()
img_car = cuadricula.scale_image(pygame, img_car, target_width=15)

#Circuit
path = os.path.join(os.path.dirname(__file__), "./assets/exercici013/circuit.png")
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
    global car

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car["direction_x"] = "left"
            elif event.key == pygame.K_RIGHT:
                car["direction_x"] = "right"
            elif event.key == pygame.K_UP:
                car["direction_y"] = "up"
            elif  event.key == pygame.K_DOWN:
                car["direction_y"] = "down"
        elif  event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if car["direction_x"] == "left":
                    car["direction_x"] = "none"
            elif event.key == pygame.K_RIGHT:
                if car["direction_x"] == "right":
                    car["direction_x"] = "none"
            elif event.key == pygame.K_UP:
                if car["direction_y"] == "up":
                    car["direction_y"] = "none"
            elif event.key == pygame.K_DOWN:
                if car["direction_y"] == "down":
                    car["direction_y"] = "none"
    return True

# Fer càlculs
def app_run():
    global car
    delta_time = clock.get_time() / 1000.0

    if car["direction_x"] == "left":
        car["x"] = car["x"]  - car["speed"] * delta_time
        car["angle"] = 90
    elif  car["direction_x"] == "right":
        car["x"] = car["x"] + car["speed"] * delta_time
        car["angle"] = -90
    
    if  car["direction_y"] == "up":
        car["y"] = car["y"] - car["speed"] * delta_time
        if car["direction_x"] == "none":
            car["angle"] = 0
        elif car["direction_x"] == "right":
            car["angle"] = 315
        elif car["direction_x"] == "left":
            car["angle"] = 45
    elif car["direction_y"] == "down":
        car["y"] = car["y"] + car["speed"] * delta_time
        if car["direction_x"] == "none":
            car["angle"] = 180
        elif car["direction_x"] == "right":
            car["angle"] = 225
        elif car["direction_x"] == "left":
            car["angle"] = 135

# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)

    screen.blit(img_circuit, (0,0))
    # dibuix
    rotate_img = pygame.transform.rotate(car["img"], car["angle"])
    rect = rotate_img.get_rect(center=(car["x"], car["y"]))
    screen.blit(rotate_img, rect)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()