import numpy as np


def half_circle(x):
    return (1 - x ** 2) ** 0.5


def half_sphere(x, y):
    return (1 - x ** 2 - y ** 2) ** 0.5

if __name__ == '__main__':

    N = 1000000
    x = np.linspace(-1, 1, N)
    dx = 2 / (N-1)  # 长度为直径2，矩阵块数为N-1
    y = half_circle(x)
    half_pi = dx * np.sum(y)
    print('  my pi = %.16f' % (half_pi * 2))
    print('real pi = %.16f' % (np.pi))
