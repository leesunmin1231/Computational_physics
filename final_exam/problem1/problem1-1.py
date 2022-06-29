import numpy as np
import matplotlib.pyplot as plt

mass = np.array([80478, 80432, 80336, 80270, 80415, 80440, 80376, 80370, 80433]) # data
exp = np.array(['A','B','C','D','E','F','G','H','I']) # x-axis or time
errors = np.array([83,79,67,55,52,51,23,19,9])
counts = []

for i in range(len(mass)):
    counts.append(int((mass[i]/errors[i])**2))

print("raw counts:" ,counts) # 1-2번 정답
plt.errorbar(exp, mass, yerr = errors, fmt='o') # data point drawing
plt.show()
# 1-2번 답: raw counts: [940152, 1036581, 1437708, 2130007, 2391483, 2487733, 12212289, 17892900, 79869969]