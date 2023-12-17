import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def solve_ex30_3(T0, TL, delta_x, delta_t, t_end):
    # input parameters
    # - T0      : fixed temperature at x=0
    # - TL      : fixed temperature at x=L
    # - delta_x : step size along x (location)
    # - delta_t : step size along t (time)
    # - t_end   : ending time

    # return value: T
    # i-th row of T: temperature distribution at time i
    # j-th column of T: temperature change at node j

    L = 10
    _lambda = 0.020875

    t = np.arange(0, t_end + delta_t, delta_t)
    x = np.arange(0, L + delta_x, delta_x)
    m = len(x) - 2
    T = np.zeros((len(t), len(x)))

    T[:, 0] = T0
    T[:, -1] = TL

    A = np.zeros((m, m))
    A[0, :2] = [1 + 2 * _lambda, -_lambda]
    for i in range(1, m - 1):
        A[i, (i - 1):(i + 2)] = [-_lambda, 1 + 2 * _lambda, -_lambda]
    A[m - 1, -2:] = [-_lambda, 1 + 2 * _lambda]

    for l in range(len(t) - 1):
        b = np.zeros((m,))
        b[0] = T[l, 1] + _lambda * T0
        b[1:m - 1] = T[l, 2:m]
        b[m - 1] = T[l, m] + _lambda * TL

        T[l + 1, 1:-1] = np.linalg.solve(A, b)

    return T


