import numpy as np
from functools import reduce

def polynomial_regression(dataset, degree):
    # input parameters
    # - dataset: n x 2 matrix (numpy.array) containing the dataset
    #  * dataset[:,0]: x-coordinates
    #  * dataset[:,1]: y-coordinates
    # - degree: polynomial degree for regression

    # return value:
    # - An array of coefficients of the fitting polynomial. (size degree+1)
    # - The array should contain the polynomial coefficients in the ascending order.
    #    [a_0,a_1,a_2,...a_d] ( d = degree )
    x = dataset[:,0]
    y = dataset[:,1]
    sx=[]
    sy=[]

    for i in range(2*degree+1):
        sx.append(reduce(lambda total, now: total + now ** i, x, 0)) #reduce는 시그마
    for j in range(degree+1):
        sy.append(np.dot(x ** j, y)) #dot은 행렬 곱 (x에 n제곱한 값들의 합 * y)

    A_Sub = []
    for i in range(degree+1):
        A_Sub.append(sx[i:i+degree+1])

    A = np.array(A_Sub)
    b = np.array(sy)

    return np.linalg.solve(A, b)  # 연립 방정식의 해


    # NOTE: You can use "np.linalg.solve" to solve a linear system.

