import numpy as np
from hw1 import *


###############################################################################
# test of the Jacobi method

def print_results(ret):
    print('+---------------------------+')
    print("| Test of the Jacobi method |")
    print('+---------------------------+')
    if ret is None:
        print('Failed: Maximum number of iterations is exceeded.')
    else:
        x = ret[0]
        niter = ret[1]
        ea = ret[2]
        print(f'numerical solution (x) = {x}')
        print(f'verification: Ax-b = {np.dot(A,x) - b}')
        print(f'number of iterations = {niter}')
        print(f'percent relative error (2-norm) = {ea}')

# Example 9.3 on p.253
A = np.array([[0.3, 0.52, 1],
              [0.5, 1,    1.9],
              [0.1, 0.3,  0.5]])
b = np.array([-0.01, 0.67, -0.44])

print_results(Jacobi(A, b, np.zeros(A.shape[0]), 10, 1e-10))

# Example 9.5 on p.259
A = np.array([[3,   -0.1, -0.2], 
              [0.1,  7,   -0.3],
              [0.3, -0.32,10]])
b = np.array([7.85, -19.3, 71.4])

print_results(Jacobi(A, b, np.zeros(A.shape[0]), 10, 1e-10))


