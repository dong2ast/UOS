import numpy as np

# 25.1 Euler's explicit method (p.722)
def Euler_explicit(f, a, b, hs, y0):
    ys = np.empty((len(hs),))
    # ys[j] contains y(b) computed with the step size hs[j].
    for j in range(len(hs)):
        h = hs[j] #step size
        x = np.arange(a,b+h,h) # x 좌표 리스트
        n = len(x) # x 좌표 개수
        y = np.zeros((n,)) # y 넣을 빈 리스트
        y[0] = y0 #y 초기값
        for i in range(n-1): # 모든 x에 대해
            slope = f(x[i],y[i])
            y[i+1] = y[i] + slope*h
        ys[j] = y[-1]
    return ys

# 25.2.1. Heun's method (p.734)
def Heun(f, a, b, hs, y0):
    ys = np.zeros((len(hs),))

    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0

        for i in range(n-1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + h, y[i] + h * k1)
            y[i + 1] = y[i] + 0.5 * h * (k1 + k2)

        ys[j] = y[-1]
    return ys

# 25.2.2. Midpoint method (p.738)
def midpoint(f, a, b, hs, y0):
    ys = np.zeros((len(hs),))

    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0

        for i in range(n - 1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
            y[i + 1] = y[i] + h * k2

        ys[j] = y[-1]
    return ys

# Ralston's method (p.744)
def Ralston(f, a, b, hs, y0):
    ys = np.zeros((len(hs),))

    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0

        for i in range(n - 1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + (2 / 3) * h, y[i] + (2 / 3) * h * k1)
            y[i + 1] = y[i] + (h / 4) * (k1 + 3 * k2)

        ys[j] = y[-1]
    return ys

# 3rd order Runge-Kutta method (classical, p.746-747)
def RK3_classical(f, a, b, hs, y0):
    ys = np.zeros((len(hs),))

    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0

        for i in range(n - 1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
            k3 = f(x[i] + h, y[i] - h * k1 + 2 * h * k2)
            y[i + 1] = y[i] + (h / 6) * (k1 + 4 * k2 + k3)

        ys[j] = y[-1]
    return ys

# 3rd order Runge-Kutta method (Nystrom's): See the slide
def RK3_Nystrom(f, a, b, hs, y0):
    ys = np.zeros((len(hs),))

    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0

        for i in range(n - 1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + (2 / 3) * h, y[i] + (2 / 3) * h * k1)
            k3 = f(x[i] + (2 / 3) * h, y[i] + (2 / 3) * h * k2)
            y[i + 1] = y[i] + (h / 4) * (k1 + 3 * k3)

        ys[j] = y[-1]
    return ys

# 25.3.3. 4th order Runge-Kutta method (classical) (p.747)
def RK4_classical(f, a, b, hs, y0):
    ys = np.zeros((len(hs),))

    for j in range(len(hs)):
        h = hs[j]
        x = np.arange(a, b + h, h)
        n = len(x)
        y = np.zeros((n,))
        y[0] = y0

        for i in range(n - 1):
            k1 = f(x[i], y[i])
            k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
            k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k2)
            k4 = f(x[i] + h, y[i] + h * k3)
            y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        ys[j] = y[-1]
    return ys


