import numpy as np
from numpy.linalg import inv
from math import *
import matplotlib.pyplot as plt

def point(angle): # 장애물을 만나기 전 공의 좌표
    x = l * sin(angle) + x_center
    y = l * cos(angle) + y_center
    return (x,y)

def point_2(angle): # 장애물을 만나고 난 뒤 공의 좌표
    x = l * sin(angle) + x_center
    y = l * cos(angle) + y_center_2
    return (x,y)

def G(t,y,df):
    F[0] = df - g*sin(y[1]) - c*y[0]
    F[1] = y[0]
    return inv_L.dot(F)

def RK4(t,y,delta_t,df):
    k1 = G(t, y, df)
    k2 = G(t+0.5*delta_t, y+0.5*delta_t*k1,df)
    k3 = G(t+0.5*delta_t, y+0.5*delta_t*k2,df)
    k4 = G(t+1.0*delta_t, y+1.0*delta_t*k3,df)
    return k1/6.0 + 2.0*k2/6.0 + 2.0*k3/6.0 + k4/6.0

width = 600
height = 400

l= 300 # pixel length

x_center=width*0.5
y_center=height*0.2
y_center_2 = 230 # y_center_2 = height*0.2 + l*0.5

g= 9.8
ll=2 # initial string length 2 meters
c=0.2 # damping term
F0 = 1.0
omega=sqrt(g/ll)

delta_t = 0.02 #time step
time = np.arange(0.0, 50.0, delta_t)

theta0=0.0*pi/180.
thetadot0=0.0

y=np.array([thetadot0,theta0])
L=np.array([[ll,0.0],[0.0,1.0]])
F=np.array([0.0,0.0])
inv_L=inv(L)
dF=0

count=0

# result list
V = [] # angular velocity
Y = [] # angle
force = []

for t in time:
    xy=point(y[1])
    xy_2 = point_2(2*y[1]) # theta0 --> 2 theta0
    t+=delta_t
    
    if t <= 28:
        if y[1] <= 0:
            dF = F0*cos(omega*t)
            if dF < 0:
                dF = 0
            c = 0.2
            l = 300
            ll = 2
        else:
            dF = 0
            c = 0.2
            l = 300
            ll = 2
    else:
        if y[1] <= 0:
            dF = 0
            c = 0.2
            l = 300
            ll = 2
        else:
            dF = 0
            c = 0.2
            l = 150
            ll = 1

    y=y+delta_t*RK4(t,y,delta_t,dF)
    count+=1
    V.append(y[0])
    Y.append(y[1]) 
    force.append(dF)


plt.grid(True)
plt.plot(time, V, 'r', label = 'Angular velocity')
plt.plot(time, Y, 'b', label = 'Angle')
plt.plot(time, force, 'g', label = 'Driving force')
plt.legend(loc = 'upper right')
plt.show()