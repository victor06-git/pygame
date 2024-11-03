#!/usr/bin/env python3

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
LIGHT_BLUE = (173, 216, 230)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

CELL_SIZE = 50

pos_skater = {"row": 0, "column": 0}

img_tree = get_emoji(pygame, "🌲", size=CELL_SIZE)
img_sman = get_emoji(pygame, "☃️", size=CELL_SIZE)
img_snow = get_emoji(pygame, "❄️", size=CELL_SIZE)
img_skater = get_emoji(pygame, "🏂", size=CELL_SIZE)

board = []
# Bucle de l'aplicació
def main():
    is_looping = True

    init_board()

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
    global pos_skater
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        if event.type == pygame.KEYUP:
            new_row = pos_skater["row"]
            new_column = pos_skater["column"]
            if event.key == pygame.K_LEFT:
                new_column -= 1
            elif  event.key == pygame.K_RIGHT:
                new_column += 1
            elif  event.key == pygame.K_UP:
                new_row -= 1
            elif   event.key == pygame.K_DOWN:
                new_row += 1

            if is_skiable_cell(new_row,new_column):
                pos_skater["row"] = new_row
                pos_skater["column"] = new_column



    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    cuadricula.draw_grid(pygame, screen, 50)

    start_x = 50
    start_y = 50
    for row in range(len(board)):
        for col in range(len(board[row])):
            x = start_x + col * CELL_SIZE
            y = start_y + row * CELL_SIZE
            pygame.draw.rect(screen, LIGHT_BLUE, (x,y, CELL_SIZE, CELL_SIZE) )

            if board[row][col] != '':
                if board[row][col] == 'T':
                    screen.blit(img_tree, (x,y, CELL_SIZE, CELL_SIZE))
                elif board[row][col] == 'M':
                    screen.blit(img_sman, (x,y, CELL_SIZE, CELL_SIZE))
                elif  board[row][col] == 'S':
                    screen.blit(img_snow, (x,y, CELL_SIZE, CELL_SIZE))
    x = start_x + pos_skater["column"] * CELL_SIZE
    y = start_y + pos_skater["row"] * CELL_SIZE
    screen.blit(img_skater, (x, y, CELL_SIZE, CELL_SIZE))

def init_board():
    global board
    rows = 8
    cols =10

    board = [['' for _ in range(cols)] for _ in range(rows)]
    place
    
    
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()