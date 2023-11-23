import numpy as np

# input parameters
# - f: function to evaluate the 1st derivative
# - x: x value where the 1st derivative is to be computed.
# - h: array of step sizes.

# return value
# - v: array of 1st derivatives.
#      v[i] is the 1st derivative computed using the step size h[i].


# Two-Points Forward Difference Formula
def forward_diff_2_points(f, x, h):
    return (f(x+h)-f(x))/h

# Two-Points Backward Difference Formula
def backward_diff_2_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return np.zeros((len(h),))

# Two-Points Central Difference Formula
def central_diff_2_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return np.zeros((len(h),))

# Three-Points Forward Difference Formula
def forward_diff_3_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return np.zeros((len(h),))

# Three-Points Backward Difference Formula
def backward_diff_3_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return np.zeros((len(h),))

# Four-Points Central Difference Formula
def central_diff_4_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return np.zeros((len(h),))




