import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-1,1,0.01)
y = np.exp(t)

plt.figure()
plt.plot(t, y, 'r')
plt.show()
