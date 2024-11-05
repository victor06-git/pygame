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

mouse_pos = { "x": -1, "y": -1 }
heights = [0] * 22 #Multiplica per 22 caselles

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
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused() #Per saber si el ratolí està sobre la finestra

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
    return True

# Fer càlculs
def app_run():
    global heights

    cell_width = 25
    cell_height = 50

    inside_cell = False
    for cnt in range(len(heights)):
        cell_x = 50  + cnt * cell_width
        cell_y_top = 250 - heights[cnt]
        cell_y_bottom = 250

        if cell_x <= mouse_pos["x"] < (cell_x + cell_width) and cell_y_top <= mouse_pos["y"] <cell_y_bottom:
            inside_cell = True
            break
    for cnt in range(len(heights)):
        cell_x = 50 + cnt * cell_width + (cell_width / 2)

        if inside_cell:
            distance = abs(cell_x - mouse_pos["x"])

            max_distance = 200
            heights[cnt] = max(5, 45 - min(distance, max_distance) * (40 / max_distance))
        else:
            heights[cnt] = 5


# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # dibuix
    for cnt in range(len(heights)):
        x = 50 + cnt * 25
        height = 5 + heights[cnt]
        y = 250 - height
        pygame.draw.rect(screen, BLACK, (x, y, 25, height))



    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()