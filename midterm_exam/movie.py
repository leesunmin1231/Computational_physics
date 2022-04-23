import pygame
import sys
import os
from math import *
import numpy as np
from numpy.linalg import inv #linear algebra

def point(angle, stop_flag):
    if t > let_obs and angle < 0 and stop_flag == 1: # 장애물을 뒀을 때, x, y 좌표.
        y = l * cos(2*angle) + y_center + (line_l/2)
        x = l * sin(2*angle) + x_center
    else:
        y = l * cos(angle) + y_center
        x = l * sin(angle) + x_center
    return (x,y)

def render(posxy, angle, stop_flag):
    obs = line_l/2
    screen.fill(white)
    if (t > let_obs and angle < 0 and stop_flag == 1): # 장애물 뒀을 때, 줄 그리기.
        pygame.draw.line(screen, black, (x_center, y_center),(x_center, y_center + l),2)
        pygame.draw.line(screen, black,(x_center,y_center + l),(posxy[0],posxy[1]),2)
    else:
        pygame.draw.line(screen, black,(x_center,y_center),(posxy[0],posxy[1]),2)
    if (t > let_obs and stop_flag == 1): # 장애물 그리기.
        pygame.draw.circle(screen, blue, (x_center, y_center + obs),5)
    pygame.draw.circle(screen, green, (posxy[0],posxy[1]),10)

def get_k(t, y, dF):
    F[0] = dF - g*sin(y[1])-c*y[0] # simple pendulum 식에 외부힘과 damping term을 추가해 주었다.
    F[1] = y[0]
    return inv(L).dot(F)

def RK4(t, y, delta_t, dF):
    k1 = get_k(t, y, dF)
    k2 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k1, dF)
    k3 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k2, dF)
    k4 = get_k(t + 1.0 * delta_t, y + 1.0 * delta_t * k3, dF)
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
line_l = 200 # length

# location of the origin
x_center = width*0.5
y_center = height*0.2


#variables
k = 5.0
g = 9.8
c = 0.1
delta_t = 0.02 #time step
t = 0.0
let_obs = 24 # 장애물을 놓는 시간.
ll = 2.0
F0 = 1.0
omega = sqrt(g/ll)
#initial condition
velocity=0.0
theta=0.0

y=np.array([velocity,theta])
L = np.array([ [ll,0.0], [0.0, 1.0]])
F = np.array([0.0,0.0]) # no driving force at the moment

count = 0 # 영상 녹화를 위해 변수 선언.
stop_flag = 0 # 외부 힘을 제거하는 시점에 1로 바꾼다.

while True:
    if count == 4000: # 반복문 탈출 조건. -> 영상길이 40초.
        break
    count+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    if (y[1] >= sqrt(3)/3): # 일정 각도를 넘어가면 드라이기 제거. stop flag를 1로 바꾸고 외부힘 0으로 설정.
        stop_flag = 1
        dF = 0 
    if (stop_flag == 0):
        dF = F0*cos(omega*t) # 외부 힘 설정 -> 시간에 따라 cos함수로 힘을 주었다.
        if dF < 0:
            dF = 0
    if (t > let_obs and y[1] < 0 and stop_flag == 1): # 일정 시간이 지나면 장애물을 둔다.
        l = line_l/2
    elif (y[1] >= 0):
        l = line_l
    xy = point(y[1], stop_flag) # updating the positions
    # angle goes in and (x,y) comes out

    render(xy, y[1], stop_flag) # you draw x,y position
    ######################################
    #block from RK4
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t, dF)
    ######################################

    clock.tick(100) #runs 1 frame per second
    pygame.display.update()
    filename = "movie_%04d.png" %(count)
    pygame.image.save(screen, filename)


# 이미지 취합하여 영상 만들기
os.system("ffmpeg -r 100 -f image2 -s 600x400 -i movie_%04d.png -vcodec libx264 -pix_fmt yuv420p movie.mp4")
# 영상 만들기에 사용된 이미지 전체 삭제. (윈도우 운영체제일 경우 rm 대신 del 을 사용해야 정상 작동한다.)
os.system("rm movie_*.png")