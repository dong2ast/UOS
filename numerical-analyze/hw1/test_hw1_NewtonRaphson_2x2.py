import numpy as np
from hw1 import *

###############################################################################
# test of the Newton-Raphson method to solve 
# a 2x2 system of nonlinear equations

def u(x,y): # (6.19a) on p.170
    return x**2 + x*y - 10

def dudx(x,y):
    return 2*x + y

def dudy(x,y):
    return x

def v(x,y): # (6.19b) on p.170
    return y + 3*x*y**2 - 57

def dvdx(x,y):
    return 3*y**2

def dvdy(x,y):
    return 1 + 6*x*y

def print_results(ret):
    print('+----------------------------------------------------+')
    print('| Test of the Newton-Raphson method for a 2x2 system |')
    print('+----------------------------------------------------+')
    if ret is None:
        print('Failed: Maximum number of iterations is exceeded.')
    else:
        x = ret[0]
        y = ret[1]
        niter = ret[2]
        ea = ret[3]
        print(f'numerical solution (x,y) = {x,y}')
        print(f'verification: u(x,y) = {u(x,y)}, v(x,y) = {v(x,y)}')
        print(f'number of iterations = {niter}')
        print(f'percent relative error = {ea}')

print_results(NewtonRaphson_2x2(u,dudx,dudy,v,dvdx,dvdy,1.5,3.5,100,1e-8))

print_results(NewtonRaphson_2x2(u,dudx,dudy,v,dvdx,dvdy,1.5,3.5,2,1e-8))


