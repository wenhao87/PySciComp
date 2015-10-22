from scipy.integrate import odeint
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def lorenz(w, t, sigma, rho, beta):

    # 给出位置矢量 w，和三个常熟参数 sigma, rho, beta，计算出 dx/dt, dy/dt, dz/dt 的值
    # 直接与lorenz的计算公式对应

    x, y, z = w
    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])

if __name__ == '__main__':

    t = np.arange(0, 30, 0.01)  # 创建时间点

    # 调用 odeint 对 lorenz 进行求解，使用两个不同的初始值
    track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0))
    track2 = odeint(lorenz, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0))

    # 绘图
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(track1[:, 0], track1[:, 1], track1[:, 2])
    ax.plot(track2[:, 0], track2[:, 1], track2[:, 2])
    plt.show()
