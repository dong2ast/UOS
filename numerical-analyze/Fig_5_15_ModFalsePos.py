import numpy as np

#def ModFalsePos(xl, xu, es, imax, xr, iter, ea):
def ModFalsePos(xl, xu, es, imax, xr):
    iter = 0
    fl = f(xl)
    fu = f(xu)
    il = 0  # The psudocode in Fig.5.15 doesn't have this initialization
    iu = 0  # The psudocode in Fig.5.15 doesn't have this initialization
    while True:
        xrold = xr
        xr = xu - fu*(xl-xu)/(fl-fu)
        fr = f(xr)
        iter = iter + 1
        if xr != 0:
            ea = np.abs((xr-xrold)/xr)*100
        test = fl*fr
        if test < 0:
            xu = xr
            fu = f(xu)
            iu = 0
            il = il + 1
            if il >= 2:
                fl = fl/2
        elif test > 0:
            xl = xr
            fl = f(xl)
            il = 0
            iu = iu + 1
            if iu >= 2:
                fu = fu/2
        else:
            ea = 0
        if (ea < es) or (iter >= imax):
            break
    return xr,iter,ea


def f(x):
    return x**10-1

xl = 0
xu = 1.3
es = 0.01
imax = 100
xr = 0

x,iter,ea = ModFalsePos(xl, xu, es, imax, xr)

print(f'Number of iterations = {iter}')
print(f'Stopping criteria = {es:.4f}%')
print(f'Approximate percent relative error = {ea:.4f}%')
print(f'x = {xr:.4f}')
print(f'f(x) = {f(x):.4e}')


