from matplotlib import pyplot as plt
import numpy as np
from math import pow, gamma
import matplotlib.pyplot as plt

def func(nu, y): # nu = ndf, y = chisquare
    norm = pow(2, nu/2.0) * gamma(nu/2.0) # denominator of normalization
    powe = np.power(y, nu/2.0 -1) # power function part
    expo = np.exp(-y/2.0) # expo. function part
    return (1.0/norm) * powe * expo

# a function
nu = 30 # ndf

y = np.linspace(0,100,1000) # 0 to 10 by 0.1 steps
f_y = func(nu, y)

# print ("X-axis values : ", y)

#drawing the function
plt.plot(y, f_y, "C4",)
plt.grid()
plt.show()
