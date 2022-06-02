import numpy as np
import matplotlib.pyplot as plt
from math import *

k = 0.1 # weak sqring const
m = 1.0
c = 1.0 #damping

omega = sqrt(k/m)
gamma = 0.5* c/m
omega_d = sqrt(omega**2 - gamma**2)

# init condition
x0 = 1.0 # 1m pull from equil
v0 = 0.0 # 0m/s init velocity

phi0 = pi/2
B_d = sqrt(x0**2 + v0**2 / omega**2)

#resulting function
t = np.linspace(0,20,1000)

x_t_under = np.exp(-gamma * t) * B_d * np.sin(omega_d *t +phi0)

#plotting
plt.plot(t, x_t_under, 'b')
plt.grid(True)
plt.title("Under damping")
plt.show()
