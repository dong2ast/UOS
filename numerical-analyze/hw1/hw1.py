import numpy as np


# The codes are to be tested with Python version 3.9

# Bracketing Method로 근 구하기 (y=0이 되는 x 좌표)
def FalsePosition(f, xl, xu, maxiter, epsilon):
    i = 0
    fl = f(xl)
    fu = f(xu)
    x = 0

    while True:
        xrold = x
        x = xu - fu * (xl - xu) / (fl - fu)
        fr = f(x)
        if x != 0:
            ea = np.abs((x - xrold) / x) * 100

        test = fl * fr
        # 왼쪽 값과 찾은 값 사이에 x축 존재 하는지 구별
        if test < 0:  # 오른쪽 이동
            xu = x
            fu = f(xu)
        elif test > 0:  # 왼쪽 이동
            xl = x
            fl = f(xl)
        else:  # 근 발견
            ea = 0

        if i >= maxiter:
            return None

        if ea < epsilon:
            break
        i += 1

    return x, i, ea
    # f: function defined in the equation "f(x)=0"
    # xl, xu: initial lower/upper bound (defined on p.136)
    # maxiter: maximum iterations
    # epsilon: termination criterion ("percent relative error" defined in (3.5) on p.62)

    # return values
    # * If the solution is found, return (x,i,ea) (a 3-tuple) where
    # - x: computed approximate solution 
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: percent relative error
    # * If the solution is not found within the maximum iterations, return None

    # NOTE: To compute the percent relative error, you need the "previous approximation"
    #       value in the formula (3.5) but we don't have any for the bracketing methods.
    #       So skip computing it in the first iteration and compute them from 
    #       the second iterations.

    # TODO: Implement the false-position method based on the formula (5.7) on p.136.


# Open Method로 근 구하기 (y=0이 되는 x좌표)
def NewtonRaphson(f, df, x0, maxiter, epsilon):
    i = 0
    fx = f(x0)
    dfx = df(x0)
    x_old = x0
    while True:
        # 다음 x 좌표 구하기
        x = x_old - fx / dfx
        print(x)
        if x != 0:
            ea = np.abs((x - x_old) / x) * 100  # - ea: percent relative error (이전 단계의 x 값에 비해 상대적인 오류)

        if i >= maxiter:
            return None
        if ea < epsilon:
            break

        # 다음 반복을 위한 설정
        x_old = x
        fx = f(x)
        dfx = df(x)
        i += 1
    return x, i, ea

    # f: function defined in the equation "f(x)=0"
    # df: derivative of f(x)
    # x0: initial estimate/guess (defined on p.152)
    # maxiter: maximum iterations
    # epsilon: termination criterion ("percent relative error" defined in (3.5) on p.62)

    # return values
    # * If the solution is found, return (x,i,ea) (a 3-tuple) where
    # - x: computed approximate solution 
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: percent relative error
    # * If the solution is not found within the maximum iterations, return None

    # TODO: Implement the Newton-Raphson method based ob the formula (6.6) on p.153.


# 접면 (z=0이 되는 x, y, 구하기)
def NewtonRaphson_2x2(u, dudx, dudy, v, dvdx, dvdy, x0, y0, maxiter, epsilon):
    # u,v: functions defined in the system of nonlinear equation (p.170)
    #       u(x,y) = 0
    #       v(x,y) = 0
    # dudx, dudy: first derivatives of u(x,y) (p.173)
    # dvdx, dvdy: first derivatives of v(x,y) (p.173)
    # x0, y0: initial estimates/guesses (defined on p.152)
    # maxiter: maximum iterations
    # epsilon: termination criterion ("percent relative error" defined in (3.5) on p.62)
    #          both x and y should meet the termination criterion.
    i = 0
    fu = u(x0, y0)
    fv = v(x0, y0)
    fdudx = dudx(x0, y0)
    fdudy = dudy(x0, y0)
    fdvdx = dvdx(x0, y0)
    fdvdy = dvdy(x0, y0)
    x_old = x0
    y_old = y0
    while True:
        # 다음 x 좌표 구하기
        x = x_old - ((fu * fdvdy) - (fv * fdudy)) / ((fdudx * fdvdy) - (fdudy * fdvdx))
        y = y_old - ((fv * fdudx) - (fu * fdvdx)) / ((fdudx * fdvdy) - (fdudy * fdvdx))
        if x != 0 and y != 0:
            ea = max(abs((x - x_old) / x) * 100,
                     abs((y - y_old) / y) * 100)  # - ea: percent relative error (이전 단계의 x 값에 비해 상대적인 오류)
        if i >= maxiter:
            return None
        if ea < epsilon:
            break

        # 다음 반복을 위한 설정
        x_old = x
        y_old = y
        fu = u(x, y)
        fv = v(x, y)
        fdudx = dudx(x, y)
        fdudy = dudy(x, y)
        fdvdx = dvdx(x, y)
        fdvdy = dvdy(x, y)
        i += 1
    return x, y, i, ea

    # return values
    # * If the solution is found, return (x,y,i,ea) (a 4-tuple) where
    # - x,y: computed approximate solutions ("None" if no solution is found within the maximum iterations)
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: largest percent relative error among x and y
    # * If the solution is not found within the maximum iterations, return None

    # TODO: Implement the Newton-Raphson method to solve a 2x2 system of nonlinear equations
    #       based on the formulas in (6.24a) and (6.24b) on p.173.



# def Muller(f, xr, h, eps, maxit):
    # f: polynomial function defined in the equation "f(x)=0"
    # xr: initial guess
    # h: value to be used to perturb xr to obtain two more initial guesses (explained on p.187)
    # eps: termination criterion
    # maxit: maximum number of iterations

    # return values
    # * If the solution is found, return (x,i,ea) (a 3-tuple) where
    # - x: computed approximate solution 
    # - i: number of iterations, starting with zero (first iteration)
    # - ea: percent relative error
    # * If the solution is not found within the maximum iterations, return None

    # TODO: Implement the pseudocode in Figure 7.4 in python3.

    # NOTE:
    # - On the 23th line in the pseudocode, 
    #   "IF(|dxr| < eps*xr OR i>=maxit) EXIT"
    #   both successful and failed cases are handled.
    #   (1) |dxr|<eps*xr  --> successful case
    #                         When exiting (returning) the function, 
    #                         the solution is stored in "xr".
    #   (2) i>=maxit   --> failed case
    #   When you implement the Muller's method, you have to handle the cases separately.

    # def GaussJordan(A,b):
    # Solve the linear system "Ax=b"

    # The following two lines are pre-implemented to provide you
    # the corresponding values in the pseudocode.

    """
    aug = np.hstack((A,b.reshape((b.shape[0], 1))))
    m,n = aug.shape
    """

    # aug: The augmented matrix [A|b]
    # m: number of rows of "aug"
    # n: number of columns of "aug"

    # TODO: Implement the pseudocode in Figure 9.10 on p.279.

    # NOTE: 
    # (1) Assume that there exists a unique solution.
    #     You don't have to handle singular cases. (Non-invertible matrix "A")
    # (2) Whenever possible, remove a loop and replace it with numpy indexing syntax.
    #     (Refer to "Fig_9_6_Gauss.py".)
    #     https://numpy.org/doc/stable/user/basics.indexing.html

# def Jacobi(A, b, x0, maxiter, epsilon):
# Solve the linear system "Ax=b"
# x0: initial guess
# maxiter: number of maximum iterations
# epsilon: termination criterion

# TODO: Implement the Jacobi method.
# Whenever possible, remove a loop and replace it with numpy indexing syntax.
# (Refer to "Fig_9_6_Gauss.py".)
# https://numpy.org/doc/stable/user/basics.indexing.html

# Bonus points: If you use ONLY ONE loop (for iterations), you can get extra points!
