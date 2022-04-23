from math import *
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv #linear algebra

def point(angle, stop_flag):
    if angle < 0 and stop_flag == 1:
        y = l * cos(2*angle) + y_center + (line_l/2)
        x = l * sin(2*angle) + x_center
    else:
        y = l * cos(angle) + y_center
        x = l * sin(angle) + x_center
    return (x,y)

def get_k(t, y, dF):
    F[0] = dF -g*sin(y[1])-c*y[0]
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

line_l = 200 # length

# location of the origin
x_center = width*0.5
y_center = height*0.2


#variables
m = 150
k = 5.0
g = 9.8
c = 0.1
delta_t = 0.02 #time step
time = np.arange(0.0, 50.0, delta_t)
ll = 2.0
F0 = 1.0
omega = sqrt(g/ll)
#initial condition
a = 0.0 # 처음 시작 각도
v0 = 0.0
#initial state
y = np.array([v0, a]) # vector [velocity, angle]
L = np.array([ [ll,0.0], [0.0, 1.0]])
F = np.array([0.0,0.0]) # no driving force at the moment
# result list
count = 0
stop_flag = 0

# result list
V = [] # angular velocity
Y = [] # angle
force = []

# time-steps aka Rk-4 method
for t in time:
    if (y[1] >= sqrt(3)/3):
        stop_flag = 1
        dF = 0
    if (stop_flag == 0):
        dF = F0*cos(omega*t)
        if dF < 0:
            dF = 0
    if (y[1] < 0 and stop_flag == 1):
        l = line_l/2
    elif (y[1] >= 0):
        l = line_l
    y = y + delta_t*RK4(t, y, delta_t, dF)
    V.append(y[0])
    Y.append(y[1]) 
    force.append(dF)


plt.grid(True)
# plt.plot(time,V, 'r', label = 'Angular velocity')
# plt.plot(time, Y, 'b', label = 'Angle')
plt.plot(time, force, 'g', label = 'Driving force')
plt.title('Driving force')
plt.legend(loc = 'upper right')
plt.show()
