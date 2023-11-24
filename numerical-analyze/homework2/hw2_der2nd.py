import numpy as np

# input parameters
# - f: function to evaluate the 1st derivative
# - x: x value where the 1st derivative is to be computed.
# - h: array of step sizes.

# return value
# - v: array of 1st derivatives.
#      v[i] is the 1st derivative computed using the step size h[i].


# Three-Points Forward Difference Formula (O(h))
def forward_diff_3_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return (f(x)-2*f(x+h)+f(x+2*h))/(h**2)

# Four-Points Forward Difference Formula (O(h^2))
def forward_diff_4_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return (2*f(x)-5*f(x+h)+4*f(x+2*h)-f(x+3*h))/(h**2)

# Three-Points Backward Difference Formula (O(h))
def backward_diff_3_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return (f(x-2*h)-2*f(x-h)+f(x))/(h**2)

# Four-Points Backward Difference Formula (O(h^2))
def backward_diff_4_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return (-f(x-3*h)+4*f(x-2*h)-5*f(x-h)+2*f(x))/(h**2)

# Three-Points Central Difference Formula
def central_diff_3_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

# Five-Points Central Difference Formula
def central_diff_5_points(f, x, h):
# TODO: Remove the following line and fill in the correct code.
    return (-f(x-2*h)+16*f(x-h)-30*f(x)+16*f(x+h)-f(x+2*h))/(12*(h**2))


