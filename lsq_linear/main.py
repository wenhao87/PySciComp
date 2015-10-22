import numpy as np
from scipy.optimize import leastsq
import pylab as pl


def fitting_func(input_x, co_P):

    # 数据拟合所用的函数
    # k * x + b

    co_k, co_b = co_P

    return co_k * input_x + co_b


def residuals(co_P, input_x, expm_y):
    return fitting_func(input_x, co_P) - expm_y


if __name__ == '__main__':

    input_x = np.linspace(-10, 10, 50)
    co_k, co_b = 2, 1                                       # 真实数据的函数参数
    real_y = fitting_func(input_x, [co_k, co_b])            # 真实数据
    expm_y = real_y + 2 * np.random.randn(len(input_x))     # 加入噪声之后的实验数据
    co_est = [0.5, 0.5]                                     # 第一次猜测的函数拟合参数

    #  调用 `leastsq' 进行数据拟合
    #   parameters:
    #       residuals:      为计算误差的函数
    #       co_est:         为拟合参数的初始值
    #       args:           为需要拟合的实验数据

    lsq_result = leastsq(residuals, co_est, args=(input_x, expm_y))

    print(u"真实参数:", [co_k, co_b])
    print(u"拟合参数:", lsq_result[0])      # 实验数据拟合后的参数

    pl.plot(input_x, real_y, 'bo')
    pl.plot(input_x, real_y, label='real curve')
    pl.plot(input_x, expm_y, 'rs', label='data with noise')
    pl.plot(input_x, fitting_func(input_x, lsq_result[0]), 'r', label='fitting curve')
    pl.legend()
    pl.show()
