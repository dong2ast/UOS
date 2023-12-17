import numpy as np
from ex30_3 import *

# delta_x = 2
delta_x = 0.5
delta_t = 0.1
# t_end = 12
t_end = 100
T0 = 100
TL = 50
L = 10

T = solve_ex30_3(T0, TL, delta_x, delta_t, t_end)

t = np.arange(0,t_end+delta_t,delta_t)
x = np.arange(0,L+delta_x, delta_x)

xx,tt = np.meshgrid(x,t)

ax = plt.axes(projection ='3d') 
ax.plot_surface(tt, xx, T, cmap=cm.coolwarm)
plt.show()



