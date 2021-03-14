import math
import matplotlib.pyplot as plt

A = [0.9, 0.7, 0.3, 0.1]
B = [1.07, 1.07, 1.07, 1.07]
C = [0.2773, 0.5, 0.1773, 0.38]
D = [0.0026, 0.003, 0.006, 0.007]

slip_x = [i for i in range(0, 100)]
labels = ["dry concrete", "wet concrete", "snow", "ice"]
friction = list()
for i in range(0, len(A)):
    friction.append([])
    for wheel_slip in slip_x:
        friction[i].append(A[i] * (B[i] * (1 - math.exp(-C[i] * wheel_slip)) - D[i] * wheel_slip))

for i in range(0, len(friction)):
    plt.plot(slip_x, friction[i], label=labels[i])

plt.xlabel('Wheel slip [%]')
plt.ylabel('Friction coefficient')

plt.legend(loc="upper right")
plt.grid()
plt.show()
