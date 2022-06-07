import numpy as np

x0 = np.array(1)
print("0th ordef tensor : ", x0, ", DIM = ", x0.ndim)
x1 = np.array([1,2,3,4])
print("1th order tensor : ", x1, ", DIM = ", x1.ndim)

x2 = np.array([[1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]])

print("2th order tensor : ",x2, ", DIM = ", x2.ndim)

x3 = np.array(
        [
            [1,2,3,4],
