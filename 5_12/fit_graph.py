import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def f(mass, a): # definition : f(mass) = a * mass + b
    return np.zeros(4) + a

counts = np.array([7,9,12,10]) # data
mass = np.array([0.5,1.5,2.5,3.5]) # x-axis or time
errors = np.sqrt(counts) # uncertainties of data

print("Data = ",counts)
print("Error on the data =", errors)
print("X axis = n", mass)

a = 0
#b = 0

start = (1) # starting position for slope and y-intersec

popt, pcov = curve_fit (f, mass, counts, sigma=errors, p0 = start, absolute_sigma=True)
print("Results Popt = ",popt)
print("Results Pcov = ",pcov)

perr = np.sqrt(np.diag(pcov)) # take the square root on the 1x1 covariance matrix = variance = error^2
print("Uncertainty = ", perr)
Nexp = f(mass, *popt) # result function mu = a line (mu = 9.147)
r = counts - Nexp # numerator in the chisquare function

chisquare = np.sum((r/errors) * (r/errors)) # chisquare function at the best fit position
print("Minimum Chisquare = ", chisquare)
plt.errorbar(mass, counts, yerr = errors, fmt='o') # data point drawing
plt.plot(mass, Nexp) # line or model drawing
plt.show()




# def f(mass, a):
#     return np.zeros(N) + a

# a= 10
# N = 4


# counts = np.array([7,9,12,10]) # data
# mass = np.array([0.5,1.5,2.5,3.5]) # x-axis or time
# error = np.sqrt(counts) # uncertainties of data

# A= f(mass, a)

# start = (1) #starting position
# popt,pcov = curve_fit(f,mass, counts,sigma = error, p0 = start, absolute_sigma=True)

# # compute chi square
# Nexp = f(mass, *popt)
# r = counts - Nexp
# chisq = np.sum((r/error)**2)
# df = N-1
# print("chisq =", chisq, "df = ",df)

# plt.errorbar(mass, counts, yerr=error, fmt = 'o')
# plt.plot(mass, Nexp)
# plt.show()