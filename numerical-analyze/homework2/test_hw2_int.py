import numpy as np
import matplotlib.pyplot as plt
from hw2_int import *


# from hw2_int_done import *

def f(x):
    return np.exp(-0.1 * x) * np.sin(3 * x) + 1


a = 0
b = 20
true_val = 20.3763385576651

powers = np.arange(0, 16)

n = len(powers)

Ns = 6 * np.power(2, powers)


def convert_data(x):
    return np.abs(np.log(x[1:] / x[:-1]) / np.log(2))


data = np.array([np.abs(true_val - composite_rectangle_left(f, a, b, Ns)),
                 np.abs(true_val - composite_midpoint(f, a, b, Ns)),
                 np.abs(true_val - composite_trapezoidal(f, a, b, Ns)),
                 np.abs(true_val - composite_Simpson_1_3rd(f, a, b, Ns)),
                 np.abs(true_val - composite_Simpson_3_8th(f, a, b, Ns))])

labels = ['Composite (Left) Rectangle (O(h))',
          'Composite Midpoint (O(h^2))',
          'Composite Trapezoidal (O(h^2))',
          'Composite Simpson''s 1/3 (O(h^4))',
          'Composite Simpson''s 3/8 (O(h^4))']

# xticks = []
# for i in range(n):
#    xticks.append(f'6*2^{powers[i]}')

fig, ax = plt.subplots(2, 1)
# plot (absolute) true error with respect to h
hsteps = np.arange(1, n + 1)
xtick_labels = map(lambda x: f'6*2^{x}', powers)
ax[0].set_title('(absolute) true error w.r.t. h')
ax[0].set_xlim(0, n + 2)
ax[0].set_xticks(ticks=hsteps, labels=xtick_labels)
ax[0].plot(hsteps, data.T, 'o-', label=labels)
ax[0].legend()

# plot the log of true relative error (log2(e_{i+1}/e_i))
# where e_i := true error for the step size 2^(-i)
hsteps = np.arange(1, n)
ax[1].set_title('log of true relative error')
ax[1].set_xlim(0, n)
ax[1].set_ylim(0, 7)
dd = convert_data(data.T)
ax[1].plot(hsteps, convert_data(data.T), label=labels)
ax[1].legend()

plt.show()
