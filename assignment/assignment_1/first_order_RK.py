import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv #linear algebra
from math import *

#variables
m = 2.0
k = 2.0

c = 0.0 #no damping
F0 = 0.0 #no damping force --> SHO

delta_t = 0.01 #time step
time = np.arange(0.0, 50.0, delta_t)

#initial condition
x0 = 1.0
v0 = 0.0

#initial state
y = np.array([v0, x0]) # vector [velocity, position]
A = np.array([[m,0.0],[0.0,1.0]])
B = np.array([[c,k],[-1.0,0.0]])
F = np.array([0.0,0.0]) # no driving force at the moment

# result list
V = [] # result velocity
Y = [] # list of positions each time interval

# time-steps aka Rk-1 method
for t in time:
    y = y + delta_t * inv(A).dot(F-B.dot(y))
    V.append(y[0])
    Y.append(y[1]) # put the position back to Y[] list

plt.grid(True)
plt.title("First order Runge Kutta")
plt.plot(time,V)
plt.show()