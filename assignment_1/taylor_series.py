import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.02)
y = np.exp(x)

plt.plot(x,y,'b')
plt.grid(True)
plt.title("Taylor series")
plt.show()