#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import cuadricula
from datetime import datetime

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
RED = (255, 69, 0) 

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Clock')

# Definir variables globals
font = pygame.font.SysFont("Arial", 16)

time = { 
    "hours": 0, 
    "minutes": 0, 
    "seconds": 0
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
    global time

    now = datetime.now()
    current_time_ms = now.timestamp() * 1000
    
    # Hores amb fracció de minuts (format 12 hores)
    time["hours"] = (current_time_ms / 3600000) % 12

    # Minuts amb fracció de segons    
    time["minutes"] = (current_time_ms / 60000) % 60

    # Segons amb fracció de mil·lisegons
    time["seconds"] = (current_time_ms / 1000) % 60
    
    

# Dibuixar
def app_draw():
    global time
    
    # Pintar el fons de blanc
    screen.fill(BLACK)

    # Dibuixar la graella
    cuadricula.draw_grid(pygame, screen, 50)

    offset = -90

    center = { "x": 325, "y": 250 }
    cord_center = (center["x"], center["y"])
    radio = 200

    graus_hora = (360/12)
    hora_angle = (graus_hora * time["hours"]) + offset
    hora = cuadricula.point_on_circle(center, radio * 0.4, hora_angle)
    hora_coord = (hora["x"], hora["y"])
    pygame.draw.line(screen, WHITE, cord_center, hora_coord, 11)
    
    graus_minut = (360/60)
    minut_angle = (graus_minut * time["minutes"]) + offset
    minut = cuadricula.point_on_circle(center, radio * 0.7, minut_angle)
    minut_coord = (minut["x"], minut["y"])
    pygame.draw.line(screen, BLUE, cord_center, minut_coord, 6)
    
    graus_segons = (360/60)
    segons_angle = (graus_segons * time["seconds"]) + offset
    segons = cuadricula.point_on_circle(center, radio * 0.9, segons_angle)
    segons_coord = (segons["x"], segons["y"])
    pygame.draw.line(screen, RED, cord_center, segons_coord, 2)
    

    for num in range(1, 13):
        angle = (graus_hora * num + offset)
        num_pos = cuadricula.point_on_circle(center, radio, angle)
        coord_pos = (num_pos["x"], num_pos["y"])
        label = font.render(str(num), True, WHITE)
        label_rect = label.get_rect(center=coord_pos)
        screen.blit(label, label_rect)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()