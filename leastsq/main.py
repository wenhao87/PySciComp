import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def fitting_func(input_x, co_array):

    # 数据拟合所用的函数: A * sin(2 * pi * k * x + theta)

    co_A, co_k, co_theta = co_array
    return co_A * np.sin(2 * np.pi * co_k * input_x + co_theta)

def residuals(co_array, input_x, exp_y):

    # 实验数据input_x, exp_y和拟合函数之间的差
    # co_array为拟合需要找到的系数

    return exp_y - fitting_func(input_x, co_array)

if __name__ == '__main__':

    input_x = np.linspace(0, -2 * np.pi, 100)
    co_A, co_k, co_theta = 10, 0.34, np.pi / 6              # 真实数据的函数参数
    real_y = fitting_func(input_x, [co_A, co_k, co_theta])  # 真实数据
    exp_y = real_y + 2 * np.random.randn(len(input_x))      # 加入噪声之后的实验数据
    co_est = [7, 0.2, 0]                                    # 第一次猜测的函数拟合参数

    #  调用 `leastsq' 进行数据拟合
    #   parameters:
    #       residuals:      为计算误差的函数
    #       co_est:         为拟合参数的初始值
    #       args:           为需要拟合的实验数据

    lsq_result = leastsq(residuals, co_est, args=(input_x, exp_y))

    print(u"真实参数:", [co_A, co_k, co_theta])
    print(u"拟合参数:", lsq_result[0])                      # 实验数据拟合后的参数

    pl.plot(input_x, real_y, label='real curve')
    pl.plot(input_x, exp_y, label='data with noise')
    pl.plot(input_x, fitting_func(input_x, lsq_result[0]), label='fitting curve')
    pl.legend()
    pl.show()
