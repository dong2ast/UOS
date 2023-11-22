import numpy as np
import matplotlib.pyplot as plt
from hw2_biquadratic_interpolation import *
#from hw2_biquadratic_interpolation_done import *


# c: data points to be interpolated.
#    c should be a 3x3 numpy array.
# c[i,j] is the value at (i,j).
# c = np.array([[-1, 1,-2],
#               [ 0, 3, 2],
#               [ 2,-1, 1]])
c = np.random.rand(3,3)    # You can test with this too.

# x & y coordinates for surface plotting
x,y = np.meshgrid(np.linspace(0,2,101),np.linspace(0,2,101))

# Evaluate the function values for all the points of the grid.
f = biquadratic(c, x.flatten(), y.flatten()).reshape(x.shape)

# Plot a 3D surface (biquadratic function)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, f)

xx,yy = np.meshgrid([0,1,2],[0,1,2])

ax.scatter(xx,yy,c.T.flatten(), c='red')

plt.show()
