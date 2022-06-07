import numpy as np
import matplotlib.pyplot as plt

def f(mass, a, b):
    return np.zeros(N) + a*mass + b
a = 10 # init. the const. function
b = 1 # y-intersect
N = 4

counts = np.array([7,9,12,10]) # data points
mass = np.array([0.5,1.5,2.5,3.5]) # mass of pumpkins
error = np.sqrt(counts) # errors poisson error 
print("Mass (x)" , mass)
print("Counts (y) ", counts)
print("Error on counts = ", error)

A = f(mass, a, b)
print(A)

start = (10,1)


from scipy.optimize import curve_fit

popt, pcov = curve_fit(f, mass, counts, sigma = error, p0 = start, absolute_sigma=True)
print(popt)
print(pcov)

perr = (np.sqrt(np.diag(pcov)))
print(perr)
print(*popt)

Nexp = f(mass, *popt)
r = counts-Nexp
chisq = np.sum((r/error)**2)
df = N - 2

print("chisq = ",chisq,",df = ",df)
plt.errorbar(mass, counts, yerr = error, fmt='o') # data point drawing
plt.plot(mass, Nexp) # line or model drawing
plt.show()
