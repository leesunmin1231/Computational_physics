import pygame
import sys
import os
from math import *
import numpy as np
from numpy.linalg import inv #linear algebra

def point(angle, stop_flag):
    if angle < 0 and stop_flag == 1:
        y = 2*l * cos(angle) + y_center
        x = x_center - sqrt(l**2 - (y - y_center - l)**2)
    else:
        y = l * cos(angle) + y_center
    x = l * sin(angle) + x_center
    return (x,y)

def render(posxy, angle, stop_flag):
    screen.fill(white)
    if (angle < 0 and stop_flag == 1):
        pygame.draw.line(screen, black, (x_center, y_center),(x_center, y_center + l),2)
        pygame.draw.line(screen, black,(x_center,y_center + l),(posxy[0],posxy[1]),2)
    else:
        pygame.draw.line(screen, black,(x_center,y_center),(posxy[0],posxy[1]),2)
    if (stop_flag == 1):
        pygame.draw.line(screen, blue, (x_center-2, y_center + 50),(x_center-2, y_center),2)
        pygame.draw.line(screen, blue, (x_center-2, y_center + 50),(x_center-52, y_center + 50),2)
        pygame.draw.line(screen, blue, (x_center-52, y_center),(x_center-52, y_center + 50),2)
        pygame.draw.line(screen, blue, (x_center-2, y_center),(x_center-52, y_center),2)
    pygame.draw.circle(screen, green, (posxy[0],posxy[1]),10)

def get_k(t, y):
    F[0] = -g*sin(y[1])
    F[1] = y[0] + F0
    return inv(L).dot(F)

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
blue = pygame.Color('blue')

# fill the screen with white color
screen.fill(white)

# update the display
pygame.display.update()

# clock for frames
clock = pygame.time.Clock()
l = 100 # length

# location of the origin
x_center = width*0.5
y_center = height*0.5


#variables
m = 150
k = 5.0
g = 9.8
delta_t = 0.02 #time step
t = 0.0
omega = sqrt(k/m)
#initial condition
a = 0.0 # 처음 시작 각도
v0 = 0.0
#initial state
y = np.array([v0, a]) # vector [velocity, angle]
L = np.array([ [1.0,0.0], [0.0, 1.0]])
F = np.array([0.0,0.0]) # no driving force at the moment
# result list
count = 0
stop_flag = 0

while True:
    if count == 1800:
        break
    count+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    if (y[1] >= sqrt(3)/3):
        stop_flag = 1
        F0 = 0
    if (stop_flag == 0):
        F0 = cos(1.2 * t)
        if F0 < 0:
            F0 = 0
    if (y[1] < 0 and stop_flag == 1):
        l = 50
    elif (y[1] >= 0):
        l = 100
    xy = point(y[1], stop_flag) # updating the positions
    # angle goes in and (x,y) comes out

    render(xy, y[1], stop_flag) # you draw x,y position

    ######################################
    #block from RK4
    if (y[1] < 0 and stop_flag == 1):
        t += delta_t / 2
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t)
    ######################################

    clock.tick(100) #runs 1 frame per second
    pygame.display.update()
    filename = "movie_%04d.png" %(count)
    pygame.image.save(screen, filename)

os.system("ffmpeg -r 100 -f image2 -s 600x400 -i movie_%04d.png -vcodec libx264 -pix_fmt yuv420p movie.mp4")
os.system("rm movie_*.png")