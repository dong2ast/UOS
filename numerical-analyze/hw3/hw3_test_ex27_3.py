from ex27_3 import *
import matplotlib.pyplot as plt

N = 100

A,b = build_linear_system(N)

T = np.empty((N+1,))
T[0] = 40   # T(0): boundary condition
T[-1] = 200 # T(10): boudnary condition
T[1:-1] = np.linalg.solve(A,b)



plt.plot(np.linspace(0,10,N+1), T, '-r')
plt.show()


