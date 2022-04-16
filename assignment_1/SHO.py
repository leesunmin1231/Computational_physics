import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

m = 1 # mass 1kg
k = 1 # spring const.1
omega = sqrt(k/m) #freq

x0 = 0.0 # init. position
v0 = 1.0 #init. velocity

t = np.linspace(0,20, 100) #time
x_t = x0 * np.cos(omega * t) + v0/omega * np.sin(omega * t) # solution

plt.plot(t, x_t)
plt.grid(True)
plt.title("Simple harmonic oscillator")
plt.show()