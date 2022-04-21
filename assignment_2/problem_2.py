import pygame
import sys
import os
from math import *
import numpy as np
from numpy.linalg import inv #linear algebra

def point(angle):
    x = l * sin(angle) + x_center
    y = l * cos(angle) + y_center
    return (x,y)

def render(posxy,angle):
    floorx = (l + 30) * sin(angle) + x_center
    floory = (l + 30) * cos(angle) + y_center
    screen.fill(white)
    pygame.draw.line(screen, black,(x_center,y_center),(posxy[0] - cos(angle) * 50,posxy[1] + sin(angle)*50),2)
    pygame.draw.line(screen, black,(x_center,y_center),(posxy[0] + cos(angle) * 50,posxy[1] - sin(angle)*50),2)
    pygame.draw.line(screen, black,(posxy[0]-cos(angle) * 80,posxy[1]+sin(angle)*80), (posxy[0]+cos(angle)*80,posxy[1]-sin(angle)*80),2)
    pygame.draw.line(screen, black,(floorx - cos(angle) * 50,floory + sin(angle) * 50),(floorx + cos(angle)*50, floory -sin(angle)*50),2)
    pygame.draw.circle(screen, green, (posxy[0]-cos(angle) * 50,posxy[1]+sin(angle)*50),5)
    pygame.draw.circle(screen, green, (posxy[0]+cos(angle) * 50,posxy[1]-sin(angle)*50),5)
    pygame.draw.line(screen, black,(posxy[0]-cos(angle) * 80,posxy[1]+sin(angle)*80),(floorx - cos(angle) * 50,floory + sin(angle) * 50),2)
    pygame.draw.line(screen, black,(posxy[0]+cos(angle)*80,posxy[1]-sin(angle)*80) ,(floorx + cos(angle)*50, floory -sin(angle)*50),2)


def get_k(t, y):
    omega = sqrt(k/m)
    F[0] = F0 * np.cos(omega * t)
    return inv(A).dot (F - B.dot(y))

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


#variables
m = 1.0
k = 5.0
c = 1.0 
F0 = 4
delta_t = 0.01 #time step
t = 0.0
omega = sqrt(k/m)
#initial condition
x0 = 1.0
v0 = 0.0
#initial state
y = np.array([v0, x0]) # vector [velocity, position]
A = np.array([[m,0.0],[0.0,1.0]])
B = np.array([[c,k],[-1.0,0.0]])
F = np.array([0.0,0.0]) # no driving force at the moment
# result list

inv_A =inv(A)

count = 0

while True:
    if count == 1800:
        break
    count+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    xy = point(y[1]) # updating the positions
    # angle goes in and (x,y) comes out

    render(xy,y[1]) # you draw x,y position

    ######################################
    #block from RK4 underdamping
    if t >= 10 and F0 > 0:
        c = 5
        F0 -= 0.5
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t)
    ######################################

    clock.tick(100) #runs 1 frame per second
    pygame.display.update()
    filename = "problem_2_%04d.png" %(count)
    pygame.image.save(screen, filename)

os.system("ffmpeg -r 100 -f image2 -s 600x400 -i problem_2_%04d.png -vcodec libx264 -pix_fmt yuv420p problem_2.mp4")
os.system("rm problem_2_*.png")