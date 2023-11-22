import matplotlib.pyplot as plt
from hw2_polynomial_regression import *
#from hw2_polynomial_regression_done import *


# NOTE: The number of data points can vary.
x = np.arange(6)
y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

dataset = np.vstack((x,y)).T

# At this point, "dataset" is an nx2 numpy.array 
# where n is the number of data points.

degree = 2  # degree of the fitting polynomial
a = polynomial_regression(dataset, degree)
# The coefficients of the fitting polynomial is stored
# in a in the ascending order.: [a_0,a_1,...,a_d] (d=degree)

print(a)

# Plot the fitting polynomial with the data points.
plt.plot(x,y,'o')
xx = np.linspace(0,5,100)
# We have to "flip" a to make it [a_d,a_{d-1},...,a_2,a_1,a_0]
# See https://numpy.org/doc/stable/reference/generated/numpy.polyval.html
plt.plot(xx,np.polyval(np.flip(a),xx),'-r') 
plt.show()


