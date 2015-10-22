from scipy.optimize import fsolve
from math import sin, cos


def func(x):

    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])

    return [5 * x1 + 3,
            4 * x0 * x0 - 2 * sin(x1 * x2),
            x1 * x2 - 1.5]


def jacobi(x):

    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [[0, 5, 0],
            [8 * x0, -2 * x2 * cos(x1 * x2), -2 * x1 * cos(x1 * x2)],
            [0, x2, x1]]

if __name__ == '__main__':

    result = fsolve(func, [1, 1, 1])
    print(result)
    print(func(result))

    jacobi_result = fsolve(func, [1, 1, 1], fprime=jacobi)
    print(jacobi_result)
    print(func(jacobi_result))

# 输出结果
# [-0.70622057 -0.6        -2.5       ]
# [0.0, -9.126033262418787e-14, 5.329070518200751e-15]
# [-0.70622057 -0.6        -2.5       ]
# [0.0, -9.126033262418787e-14, 5.329070518200751e-15]
