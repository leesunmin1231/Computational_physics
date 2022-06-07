import pygame
import sys
from math import *
import numpy as np
from numpy.linalg import inv #linear algebra

def point(angle1, angle2):
    x1 = 100 * l1 * sin(angle1) + x_center
    y1 = 100 * l1 * cos(angle1) + y_center
    x2 = x1+100*l2*sin(angle2)
    y2 = y1+100*l2*cos(angle2)
    return (x1,y1),(x2,y2)

def render(posxy1, posxy2):
    screen.fill(white)
    pygame.draw.line(screen, black,(x_center,y_center),(posxy1[0],posxy1[1]),2)
    pygame.draw.circle(screen, green, (posxy1[0],posxy1[1]),10)

    pygame.draw.line(screen, black,(posxy1[0],posxy1[1]),(posxy2[0],posxy2[1]),2)
    pygame.draw.circle(screen, green, (posxy2[0],posxy2[1]),10)

def get_k(t, y):
    F[0] = -m2 * l2 *y[1]*y[1]*sin(y[2] - y[3]) - (m1+m2)*g*sin(y[2])
    F[1] = l1*y[0]*y[0]*sin(y[2] - y[3]) - g *sin(y[3])
    F[2] = y[0]
    F[3] = y[1]

    L = np.array([
        [(m1+m2)*l1, m2*cos(y[2]-y[3]), 0, 0],
        [l1*cos(y[2]-y[3]), l2, 0, 0],
        [0,0,1,0],
        [0,0,0,1]
    ])
    return inv(L).dot(F)

def RK4(t, y, delta_t):
    k1 = get_k(t, y)
    k2 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = get_k(t + 1.0 * delta_t, y + 1.0 * delta_t * k3)
    G = 1/6.0 * k1 + 2.0/6.0 * k2 + 2.0/6.0 * k3 + 1.0/6.0 * k4
    return (G)


#canvas size
width = 1000
height = 800 

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

# location of the origin
x_center = width*0.5
y_center = height*0.5


g = 9.8
l1 = 1.0 # length of the pendulum
l2 = 1.5
m1 = 2.0
m2 = 1.0
l_pixel = 100


t = 0.0
delta_t = 0.01
y = np.array([0.0, 0.0, 1.5, 2.0]) # [angular speed, angle]
F = np.array([0.0, 0.0, 0.0, 0.0])


count = 0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    xy1, xy2 = point(y[2], y[3]) # updating the positions
    # angle goes in and (x,y) comes out

    render(xy1, xy2) # you draw x,y position

    ######################################
    #block from RK4 simple pendulum
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t)
    ######################################

    clock.tick(100) #runs 1 frame per second
    pygame.display.update()