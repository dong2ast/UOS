import numpy as np
from hw1 import *


###############################################################################
# test of the Gauss-Jordan elimination

def print_results(x):
    print('+--------------------------------------------------+')
    print("| Test of the Gauss-Jordan method without pivoting |")
    print('+--------------------------------------------------+')

    print(f'numerical solution (x) = {x}')
    print(f'verification: Ax-b = {np.dot(A, x) - b}')
    print(f'verification: 2-norm of (Ax-b) = {np.linalg.norm(np.dot(A,x)-b)}')

# Example 9.3 on p.253
A = np.array([[0.3, 0.52, 1],
              [0.5, 1,    1.9],
              [0.1, 0.3,  0.5]])
b = np.array([-0.01, 0.67, -0.44])

print_results(GaussJordan(A, b))

# Example 9.5 on p.259
A = np.array([[3,   -0.1, -0.2], 
              [0.1,  7,   -0.3],
              [0.3, -0.32,10]])
b = np.array([7.85, -19.3, 71.4])

print_results(GaussJordan(A, b))


