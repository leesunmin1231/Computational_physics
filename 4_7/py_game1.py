import pygame
import sys


#canvas size
width = 600
height = 400 

# making the canvas 600*400
screen = pygame.display.set_mode((width,height))

# predefined colors
white = pygame.Color('white')
black = pygame.Color('black')

# fill the screen with white color
screen.fill(white)

# update the display
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    # rendering
    screen.fill(white)
    pygame.draw.line(screen, black, (300,200),(300,300),2)
    pygame.draw.circle(screen, black, (300,300),10)
    pygame.display.update()