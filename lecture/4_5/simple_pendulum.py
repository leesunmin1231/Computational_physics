import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from math import *

#Slope(G) function
def ZZ(t,y):
    F[0] = -g*y[1]
    #F[0] = -g*sin(y[1]) # -g sin(theta)
    F[1] = y[0] #angular speed
    return inverse_L.dot(F)

def RK4(t, y, delta_t):
    k1 = ZZ(t, y)
    k2 = ZZ(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = ZZ(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = ZZ(t + 1.0 * delta_t, y + 1.0 * delta_t * k3)
    G = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4
    return (G)

g = 9.8 # gravity const
l = 1.0 # length

omega = sqrt(g/l)
delta_t = 0.01
time = np.arange(0,5,delta_t) # zero to 5 sec by 0.01 increment

theta0 = 10.0 * pi /180 # this is in radian
thetadot0 = 0 # of course this is too

y = np.array([thetadot0, theta0]) # vector [angular velocity, angle] 
#y[0] angular velocity
#y[1] angle

L = np.array([[l,0.0],[0.0,1.0]])
F = np.array([0.0, 0.0]) #not a force

ANGLE =[]
AS = [] #angle speed

inverse_L =inv(L)

for t in time:
    y = y + delta_t * RK4(t,y, delta_t)
    AS.append(y[0])
    ANGLE.append(y[1])

plt.plot(time, ANGLE)
plt.show()