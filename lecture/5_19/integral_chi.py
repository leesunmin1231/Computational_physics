import imp
from math import pow, exp, gamma, inf
from scipy.integrate import quad

def func (x, nu):
    norm = pow(2, nu/2.0) * gamma(nu/2.0)
    powe = pow(x, nu/2.0-1)
    expo = exp(-x/2.0)
    return (1.0/norm)*powe * expo

nu = 3
minchisquare = 1.41
I = quad(func, minchisquare, +inf, args = (nu))
print("Integral = ",I)