import numpy as np
#20182326

#1
result=((2+0j)*(1+8j))/((2+3j)*(2+6j))
print(result)

#2
A=np.array([[2,0],[1,8]])@np.array([[2,3],[2,6]])
print(A)
print(A.sum())