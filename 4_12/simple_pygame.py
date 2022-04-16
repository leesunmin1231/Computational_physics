import pygame
import sys
from math import *
import numpy as np
from numpy.linalg import inv #linear algebra

def point(angle):
    x = l * sin(angle) + x_center
    y = l * cos(angle) + y_center
    return (x,y)

def render(posxy):
    screen.fill(white)
    pygame.draw.line(screen, black,(x_center,y_center),(posxy[0],posxy[1]),2)
    pygame.draw.circle(screen, green, (posxy[0],posxy[1]),10)

def get_k(t, y):
    F[0] = -g*sin(y[1])
    F[1] = y[0]
    return inv_L.dot(F)

def RK4(t, y, delta_t):
    k1 = get_k(t, y)
    k2 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = get_k(t + 1.0 * delta_t, y + 1.0 * delta_t * k3)
    G = 1/6.0 * k1 + 2.0/6.0 * k2 + 2.0/6.0 * k3 + 1.0/6.0 * k4
    return (G)


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


g = 9.8
ll = 1.0 # length of the pendulum
t = 0.0
delta_t = 0.01
y = np.array([0.0,1.0]) # [angular speed, angle]
L = np.array([ [ll,0.0], [0.0, 1.0]])
F = np.array([0.0, 0.0])
inv_L = inv(L)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    xy = point(y[1]) # updating the positions
    # angle goes in and (x,y) comes out

    render(xy) # you draw x,y position

    ######################################
    #block from RK4 simple pendulum
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t)
    ######################################

    clock.tick(100) #runs 1 frame per second
    pygame.display.update()