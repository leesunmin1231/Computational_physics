import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 1 # weak sqring const
m = 1.0
c = 10.0 #damping
c_crit = 2

omega = sqrt(k/m)
gamma = 0.5* c/m
q = sqrt(gamma**2 - omega**2)

# init condition
x0 = 1.0 # 1m pull from equil
v0 = 0.0 # 0m/s init velocity

t = np.linspace(0,100,100)

#const
A_1 = 0.5 *((1+gamma/q)*x0 + v0/q)
A_2 = 0.5 *((1-gamma/q)*x0 - v0/q)

#final result
x_t = A_1 *np.exp(-(gamma - q)*t) + A_2 * np.exp(-(gamma + q)*t)
gamma_crit = 0.5 * c_crit/m

A = gamma_crit *x0 + v0
B = x0
x_t_crit = A * t * np.exp(-gamma_crit * t) + B *np.exp(-gamma_crit * t)

#plotting
#plt.grid(True)
plt.plot(t, x_t, 'r', t, x_t_crit, 'b')
#plt.ylim(-1,2)
plt.show()