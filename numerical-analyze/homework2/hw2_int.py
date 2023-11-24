import numpy as np


# input parameters
# - f: function to integrate
# - a,b: integration interval
# - Ns: array of number of segments

# return value
# - I: integral values (of type numpy.array)
#      I[i] is the integral values using Ns[i] number of segments

# Composite Rectangle Method with left point
def composite_rectangle_left(f, a, b, Ns):
    result = np.zeros_like(Ns, dtype=float)

    for i, N in enumerate(Ns):
        interval = (b - a) / N
        integration = 0

        for j in range(N):
            integration += f(a + (j * interval))

        integration *= interval
        result[i] = integration

    return result


# Composite Midpoint Method
def composite_midpoint(f, a, b, Ns):
    result = np.zeros_like(Ns, dtype=float)

    for i, N in enumerate(Ns):
        interval = (b - a) / N
        integration = 0

        for j in range(N):
            integration += f((a + interval / 2) + j * interval)

        integration *= interval
        result[i] = integration

    return result


# Composite Trapezoidal Method
def composite_trapezoidal(f, a, b, Ns):
    result = np.zeros_like(Ns, dtype=float)

    for i, N in enumerate(Ns):
        interval = (b - a) / N
        integration = f(a) + f(b)

        for j in range(1, N):
            integration += 2 * f(a + j * interval)

        integration *= interval / 2
        result[i] = integration

    return result


# Composite Simpson's 1/3 Method
def composite_Simpson_1_3rd(f, a, b, Ns):
    result = np.zeros_like(Ns, dtype=float)

    for i, N in enumerate(Ns):
        interval = (b - a) / N
        integration = f(a) + f(b)

        for j in range(1, N):
            k = a + j * interval

            if j % 2 == 0:
                integration += 2 * f(k)
            else:
                integration += 4 * f(k)

        integration *= interval / 3
        result[i] = integration

    return result


# Composite Simpson's 3/8 Method
def composite_Simpson_3_8th(f, a, b, Ns):
    result = np.zeros_like(Ns, dtype=float)

    for i, N in enumerate(Ns):
        interval = (b - a) / N
        integration = f(a) + f(b)

        for j in range(1, N):
            k = a + j * interval

            if j % 3 == 0:
                integration += 2 * f(k)
            else:
                integration += 3 * f(k)

        integration *= 3 * interval / 8
        result[i] = integration

    return result
