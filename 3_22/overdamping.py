import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 0.1 # weak sqring const
m = 1
c = 1 #damping

omega = sqrt(k/m)
gamma = 0.5* c/m
q = sqrt(gamma**2 - omega**2)

# init condition
x0 = 1.0 # 1m pull from equil
v0 = 0.0 # 0m/s init velocity

t = np.arange(0,100,1)

#const
A_1 = 0.5 *((1+gamma/q)*x0 + v0/q)
A_2 = 0.5 *((1-gamma/q)*x0 - v0/q)

#final result
x_t = A_1 *np.exp(-(gamma - q)*t) + A_2 * np.exp(-(gamma + q)*t)

#plotting
#plt.grid(True)
plt.plot(t, x_t)
#plt.ylim(-1,2)
plt.show()
