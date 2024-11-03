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
GOLD = (255, 215, 0)
NAVY = (0, 0, 128)

pygame.init()
clock = pygame.time.Clock()

point = {"x": -1,"y": -1}
rectangles = [
    { "rect": { "x": 50, "y": 100, "width": 250, "height": 50 }, "color": RED },
    { "rect": { "x": 50, "y": 200, "width": 100, "height": 200 }, "color": GOLD },
    { "rect": { "x": 200, "y": 200, "width": 100, "height": 100 }, "color": BLUE },
    { "rect": { "x": 200, "y": 350, "width": 400, "height": 50 }, "color": PURPLE },
    { "rect": { "x": 350, "y": 100, "width": 50, "height": 200 }, "color": ORANGE },
    { "rect": { "x": 450, "y": 100, "width": 150, "height": 100 }, "color": GREEN },
    { "rect": { "x": 450, "y": 250, "width": 150, "height": 50 }, "color": NAVY }
]
square_clicked = -1



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
    global point
    mouse_inside = pygame.mouse.get_focused() #Indica si el ratolí está en la finestra
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif  event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                point["x"] = event.pos[0]
                point["y"] = event.pos[1]
            else:
                point["x"] = -1
                point["y"] = -1
    return True
    
# Fer càlculs
def app_run():
    global point, square_clicked
    for index in range(len(rectangles)):
            rect = rectangles[index]
            if cuadricula.is_point_in_rect(point, rect["rect"]):
                square_clicked = index
    

# Dibuixar
def app_draw():
    global square_clicked
    #Centre pantalla
    
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella de coordenades (llibreria utils)
    cuadricula.draw_grid(pygame, screen, 50)
    # quadres
    
    
    color = BLACK
    for index in range (len(rectangles)):
        rect =  rectangles[index]
        rectangle = rect["rect"]
        rectangle_1 = (rectangle["x"], rectangle["y"], rectangle["width"], rectangle["height"])
        
        if square_clicked == index:
            pygame.draw.rect(screen, rect["color"], rectangle_1)
        
        pygame.draw.rect(screen, BLACK, rectangle_1, 5)
        
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()