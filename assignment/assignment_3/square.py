import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(F, a,b): # definition : f(mass) = a * mass + b
    return np.zeros(11) + a * F + b
# L = a*F +b
# (L-b)/a
# spring strech data for each force
Fdata = np.array([2,4,6,8,10,12,14,16,18,20,22])
Ldata = np.array([15,32,49, 64, 79, 98, 112, 126, 149, 175, 190])

Ldata = Ldata/1000. #milimeters -> meters

plt.figure()
plt.axis([0,25,0,0.2])

# brute force fit with the following model : f = ax+b
# we change a and b for a given x
 
mini = 9999 # mininum

for a in range(500, 1500,1):
    # print (a)
    a = a/100000.
    for b in range(-50, 150, 1):
        b = b/1000
        s = 0.0 # initialize s value
        for i in range(11):
            x = 2 *(i+1)
            ff = a*x+b
            s+=(Ldata[i]-ff)*(Ldata[i]-ff)
        if (s<mini):
            mini = s
            Nexp = f(Fdata, a,b)
            k_value = 1/a
            force105 = (0.105 - b)/a
            #print(a,b,1./a, -b/a,s)
#(d)
print("k:" ,k_value)
#(e)
print("Force when 105mm:",force105)

#(a)
plt.plot(Fdata,Ldata,"ro")
#(b)
plt.plot(Fdata, Nexp, 'b')
plt.show()

# (C). 직선 그래프를 그릴 때, 모든 데이터 포인터를 사용하지 않고 각각의 데이터에서 최소거리를 찾아 직선으로 plot해야한다.


        