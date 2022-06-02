import numpy as np
import matplotlib.pyplot as plt

#variables
m = 2.0
k = 2.0 

#x_axis
delta_t = 0.01 #time step
time = np.arange(0.0, 40.0, delta_t)

#initial condition
x0, v0 = 1.0, 0.0

#states
x,v = x0, v0

#result list
X = [] #updated position
V = [] #updated speed

#time_steps

for t in time:
    v = v + delta_t *(-k/m)*x
    x = x + delta_t * v
    X.append(x)
    V.append(v)

# plot the results
plt.grid(True)
plt.plot(time, X, 'r', time, V, 'b')
plt.show()