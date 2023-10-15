import numpy as np
import matplotlib.pyplot as plt

t = 10
g = 9.81
v = 40
m = 68.1

# (PT2.4) on p.191
def f(c):
    return (g*m/c)*(1 - np.exp(-(c/m)*t)) - v

xl = 12
xu = 16
xt = 14.8011 # 
xrold = None
ea = None

print('iteration    xl      xu      xr    ea(%)  et(%)')
print('--------- ------- ------- ------- ------ ------')

list_ea = []
list_et = []

for i in range(1,7):
    xr = (xl+xu)/2
    et = abs((xr-xt)/xt)*100
    if xrold:
        ea = abs((xr-xrold)/xr)*100
        print(f'     {i}    {xl:.4f} {xu:.4f} {xr:.4f} {ea:.4f} {et:.4f}')
    else:
        print(f'     {i}    {xl:.4f} {xu:.4f} {xr:.4f}        {et:.4f}')
    sign = f(xl)*f(xr)
    if sign < 0:
        xu = xr
    elif sign > 0:
        xl = xr
    else:
        ea = 0 # f(xr)=0

    xrold = xr
    list_ea.append(ea)
    list_et.append(et)

fig, ax = plt.subplots()

plt.yscale('log')

ax.plot(np.arange(1,7), list_ea, label='approximate')
ax.plot(np.arange(1,7), list_et, label='true')

ax.legend(loc="upper right")

plt.show()

