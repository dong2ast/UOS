import numpy as np
from hw1 import *


###############################################################################
# test of the false-position method

# 이런 함수가 있다
def f(c):  # Example 5.1 on p.124 and (PT2.4) on p.119
    t = 10
    g = 9.81
    v = 40
    m = 68.1
    return (g*m/c)*(1 - np.exp(-(c/m)*t)) - v

# 이런 함수가 있다
def g(x):  # Example 6.3 on p.153
    return np.exp(-x) - x

def print_results(ret):
    print('+-----------------------------------+')
    print('| Test of the False Position method |')
    print('+-----------------------------------+')
    if ret is None:
        print('Maximum number of iterations is exceeded.')
    else:
        x = ret[0]
        niter = ret[1]
        ea = ret[2]
        print(f'numerical solution (x) = {x}')
        print(f'verification: f(x) = {f(x)}')
        print(f'number of iterations = {niter}')
        print(f'percent relative error = {ea}')

# 함수, 시작위치, 시작위치, 최대 반복, 앱실론 값
print_results(FalsePosition(f, 12, 16, 100, 1e-5))

print_results(FalsePosition(g, -1, 2, 100, 1e-5))

print_results(FalsePosition(f, 12, 16, 2, 1e-5))



