import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import *

def f(mass, a): # definition : f(mass) = a * mass + b
    return np.zeros(N) + a

def func(x,nu):
    norm = pow(2,nu/2.0) * gamma(nu/2.0)
    powe = pow(x,nu/2.0-1)
    expo = exp(-x/2.0)
    return (1./norm) * powe * expo

N = 9
nu = N-1
I = quad(func, 21.666, inf, args=(nu))
print("I = ",I)

mass = np.array([80478, 80432, 80336, 80270, 80415, 80440, 80376, 80370, 80433]) # data
exp = np.array([1,2,3,4,5,6,7,8,9]) # x-axis or time
errors = np.array([83,79,67,55,52,51,23,19,9])

a = -1

start = (10) # starting position for slope and y-intersec

popt, pcov = curve_fit (f, exp, mass, sigma=errors, p0 = start, absolute_sigma=True)

perr = np.sqrt(np.diag(pcov)) # take the square root on the 1x1 covariance matrix = variance = error^2
print("Error = ", perr)
Nexp = f(exp, *popt) # result function mu = a line (mu = 9.147)
r = mass - Nexp 

chisquare = np.sum((r/errors) * (r/errors)) # chisquare function at the best fit position
print("Minimum Chisquare = ", chisquare)