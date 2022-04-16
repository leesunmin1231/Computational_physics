import pygame
import sys
from math import *


#canvas size
width = 600
height = 400 

# making the canvas 600*400
screen = pygame.display.set_mode((width,height))

# predefined colors
white = pygame.Color('white')
black = pygame.Color('black')
green = pygame.Color('green')

# fill the screen with white color
screen.fill(white)

# update the display
pygame.display.update()

# clock for frames
clock = pygame.time.Clock()
l = 100 # length
a = 0.0 # initial angle

# location of the origin
x_center = width*0.5
y_center = height*0.5

# infinite loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # updating the positions
    x = l * sin(a) + x_center # from the center
    y = l * cos(a) + y_center # from the center
    # rendering
    screen.fill(white)
    pygame.draw.line(screen, black, (x_center, y_center),(x,y),2)
    pygame.draw.circle(screen, green, (x,y), 10)

    clock.tick(1) # runs 1 frame per second
    pygame.display.update()

