import numpy as np
import functools
import matplotlib.pyplot as plt
from ode_solvers import *

powers = np.arange(1,5+1)
n = len(powers)

a = 0
b = 2.5

# array of h = [1/2, 1/2^2, 1/2^3, ...]
hs = np.power(2.0, -powers)

def f(x,y):
    return -1.2*y + 7*np.exp(-0.3*x)

y_init = 3

def y_true(x):
    return (70/9)*np.exp(-0.3*x) - (43/9)*np.exp(-1.2*x)


N_methods = 7   # number of methods

data = np.zeros((N_methods, n))

data[0,:] = np.abs(y_true(b) - Euler_explicit(f, a, b, hs, y_init))
data[1,:] = np.abs(y_true(b) - Heun(f, a, b, hs, y_init))
data[2,:] = np.abs(y_true(b) - midpoint(f, a, b, hs, y_init))
data[3,:] = np.abs(y_true(b) - Ralston(f, a, b, hs, y_init))
data[4,:] = np.abs(y_true(b) - RK3_classical(f, a, b, hs, y_init))
data[5,:] = np.abs(y_true(b) - RK3_Nystrom(f, a, b, hs, y_init))
data[6,:] = np.abs(y_true(b) - RK4_classical(f, a, b, hs, y_init))


fig,ax = plt.subplots(2,1)
colors = ['red', 'blue', 'green', 'black', 'cyan', 'magenta', 'yellow']
labels = ["Euler's explicit (O(h))",
                "Heun's method (O(h^2))",
                "Midpoint method (O(h^2))",
                "Ralston's method (O(h^2))",
                "RK3 (classical) (O(h^3))",
                "RK3 (Nystrom''s) (O(h^3))",
                "RK4 (classical) (O(h^4))"]

# plot (absolute) true error with respect to h
hsteps = np.arange(n)


def convert_data(x):
    return np.abs(np.log(x[1:]/x[:-1]))/np.log(2)

for i in range(N_methods):
    ax[0].plot(hsteps, data[i,:], label=labels[i], color=colors[i])
    ax[1].plot(hsteps[:-1], convert_data(data[i,:]), label=labels[i], color=colors[i])
    
xtick_labels = map(lambda x: f'2^{-x}', list(powers))
ax[0].set_title('(absolute) true error w.r.t. h')
ax[0].set_xticks(ticks=hsteps, labels=xtick_labels)
ax[1].set_title('log of true relative error')
ax[0].legend()
ax[1].legend()
plt.show()


