import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.02)
z = 1 + x + 0.5*x*x + 1/6*x*x*x + 1/24 *x*x*x*x 
y = np.exp(x)

plt.plot(x,z,'r',x,y,'b')
plt.show()