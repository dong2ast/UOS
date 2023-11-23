import numpy as np
import functools
import matplotlib.pyplot as plt
from hw2_der1st import *
#from hw2_der1st_done import *

x0 = 2  # the point of which derivative is to be evaluated

powers = np.arange(1,11)

n = len(powers)

# array of stepsizes: [1/2, 1/2^2, 1/2^3, ..., 1/2^n]
hs = np.power(2.0, -powers)

# f(x)
def f(x):
    return np.power(2.0,x)/x

# f'(x): true 1st derivative function of f(x)
def f_I(x):
    return np.power(2.0,x)*np.log(2)/x - np.power(2.0,x)/np.power(x,2.0)

def convert_data(x):
    return np.abs(np.log(x[1:]/x[:-1])/np.log(2))

true_val = f_I(x0)  # exact value

data = np.array([   np.abs(true_val - forward_diff_2_points(f, x0, hs)),
                    np.abs(true_val - forward_diff_3_points(f, x0, hs)),
                    np.abs(true_val - backward_diff_2_points(f, x0, hs)),
                    np.abs(true_val - backward_diff_3_points(f, x0, hs)),
                    np.abs(true_val - central_diff_2_points(f, x0, hs)),
                    np.abs(true_val - central_diff_4_points(f, x0, hs))])

# At this point, data is a 6xn numpy.array where
# data[i,j] is the 1st derivative computed by the i-th method with the step size hs[j].

labels = [  'Two-Points Forward Difference (O(h))',
            'Three-Points Forward Difference (O(h^2))',
            'Two-Points Backward Difference (O(h))',
            'Three-Points Backward Difference (O(h^2))',
            'Two-Points Central Difference (O(h^2))',
            'Four-Points Central Difference (O(h^4))']

fig,ax = plt.subplots(2,1)

# plot (absolute) true error with respect to h
hsteps = np.arange(1,n+1)
# tick labels for the x-axis
xtick_labels = map(lambda x: f'2^{-x}', list(powers))
ax[0].set_title('(absolute) true error w.r.t. h')
ax[0].set_xlim(0,n+2)
ax[0].set_xticks(ticks=hsteps, labels=xtick_labels)
ax[0].plot(hsteps, data.T, 'o-', label=labels)
ax[0].legend()

# plot the log of true relative error (log2(e_{i+1}/e_i))
# where e_i := true error for the step size 2^(-i)
hsteps = np.arange(1,n)
ax[1].set_title('log of true relative error')
ax[1].set_xlim(0,n)
ax[1].set_ylim(0,7)
dd = convert_data(data.T)
ax[1].plot(hsteps, convert_data(data.T), label=labels)
ax[1].legend()

plt.show()

