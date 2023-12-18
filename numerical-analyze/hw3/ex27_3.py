import numpy as np


def build_linear_system(N):
    # input parameters:
    # N: number of segments. Therefore, there are (N+1) nodes.
    # return value: tuple (A,b) for the linear system of the "interior nodes"
    # - A: coefficient matrix
    # - b: constant column vector

    # below is the list of constants in Example 27.1 (p.795)
    h_prime = 0.01  # = h' 
    Ta = 20         
    T1 = 40         # = T(0): boundary condition
    T2 = 200        # = T(10): boundary condition
    L = 10          # length of the rod

    h = L / N

    A = np.zeros((N - 1, N - 1))

    for i in range(N - 1):
        A[i, i] = -2 / h ** 2
        if i > 0:
            A[i, i - 1] = 1 / h ** 2
        if i < N - 2:
            A[i, i + 1] = 1 / h ** 2

    b = -h_prime ** 2 / h ** 2 * np.ones(N - 1)

    b[0] -= T1 / h ** 2
    b[N - 2] -= T2 / h ** 2

    return (A, b)

