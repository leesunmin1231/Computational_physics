import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv #linear algebra
from math import *

def get_k(t, y):
    omega = sqrt(k/m)
    F[0] = F0 * np.cos(omega * t)
    return inv(A).dot (F - B.dot(y))

def RK4(t, y, delta_t):
    k1 = get_k(t, y)
    k2 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = get_k(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = get_k(t + 1.0 * delta_t, y + 1.0 * delta_t * k3)
    G = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4
    return (G)

#variables
m = 1.0
k = 5.0

c = 1 #no damping
F0 = 0.0 #no damping force --> SHO

delta_t = 0.01 #time step
time = np.arange(0.0, 50.0, delta_t)

#initial condition
x0 = 1.0
v0 = 0.0

#initial state
y = np.array([v0, x0]) # vector [velocity, position]
y_first = np.array([v0, x0]) # vector [velocity, position]
A = np.array([[m,0.0],[0.0,1.0]])
B = np.array([[c,k],[-1.0,0.0]])
F = np.array([0.0,0.0]) # no driving force at the moment

# result list
V = [] # result velocity
V_first = []
Y = [] # list of positions each time interval

# time-steps aka Rk-1 method
for t in time:
    y = y + delta_t * RK4(t, y, delta_t)
    y_first = y_first + delta_t * inv(A).dot(F-B.dot(y_first))
    V_first.append(y_first[0])
    V.append(y[0])
    Y.append(y[1]) # put the position back to Y[] list

plt.grid(True)
plt.plot(time,Y, 'r', time, Y, 'b')
plt.show()