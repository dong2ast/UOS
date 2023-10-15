import numpy as np
from hw1 import *


###############################################################################
# test of the Muller's method

def f(x):  # Example 7.2 on p.186
    return x**3 - 13*x - 12

def g(x): 
    return 2.7*x**3 + 2.125*x**2 - 3.875*x + 1.25

def print_results(ret):
    print('+-----------------------------+')
    print("| Test of the Muller's method |")
    print('+-----------------------------+')
    if ret is None:
        print('Failed: Maximum number of iterations is exceeded.')
    else:
        x = ret[0]
        niter = ret[1]
        print(f'numerical solution (x) = {x}')
        print(f'verification: f(x) = {f(x)}')
        print(f'number of iterations = {niter}')


print_results(Muller(f, 5.5, 0.1, 1e-8, 100))

print_results(Muller(f, 5.5, 0.1, 1e-8, 2))



