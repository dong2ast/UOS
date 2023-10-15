import numpy as np
from hw1 import *


###############################################################################
# test of the Newton-Raphson method

def f(c):  # Example 5.1 on p.124 and (PT2.4) on p.119
    t = 10
    g = 9.81
    v = 40
    m = 68.1
    return (g*m/c)*(1 - np.exp(-(c/m)*t)) - v

def df(c):
    t = 10
    g = 9.81
    v = 40
    m = 68.1
    return  -(2*g*m/(c**2))*(1 - np.exp(-(c/m)*t)) + (g*t/c)*np.exp(-(c/m)*t)

def g(x):  # Example 6.3 on p.153
    return np.exp(-x) - x

def dg(x): # Example 6.3 on p.153
    return -np.exp(-x) - 1

def print_results(ret):
    print('+-----------------------------------+')
    print('| Test of the Newton-Raphson method |')
    print('+-----------------------------------+')
    if ret is None:
        print('Failed: Maximum number of iterations is exceeded.')
    else:
        x = ret[0]
        niter = ret[1]
        ea = ret[2]
        print(f'numerical solution (x) = {x}')
        print(f'verification: f(x) = {f(x)}')
        print(f'number of iterations = {niter}')
        print(f'percent relative error = {ea}')

print_results(NewtonRaphson(f, df, 10, 100, 1e-17))

print_results(NewtonRaphson(g, dg, 0, 100, 1e-17))

print_results(NewtonRaphson(f, df, 10, 10, 1e-17))


