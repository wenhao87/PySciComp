# -*- coding: utf-8 -*-
import scipy.weave as weave
import numpy as np
import time


def weave_sum(arr):

    size = int(len(arr))
    c_code = """
        int i;
        double counter = 0;
        for(i = 0; i < size; i++){
            counter = counter + arr(i);
        }
        return_val = counter;
        """
    err = weave.inline(c_code, ['arr', 'size'],
                       type_converters=weave.converters.blitz, compiler="gcc")

    return err

arr = np.arange(0, 10000000, 1.0)
# 先调用一次weave_sum
# Weave会自动对C语言进行编译，此后直接运行编译之后的代码
weave_sum(arr)

# Case 1: inline weave
start = time.clock()
for i in range(100):
    weave_sum(arr)  # 直接运行编译之后的代码
print(" weave_sum:", (time.clock() - start) / 100.0)

# Case 2: numpy sum
start = time.clock()
for i in range(100):
    np.sum(arr)    # numpy中的sum，其实现也是C语言级别
print(" numpy_sum:", (time.clock() - start) / 100.0)

# Case 3: Python built-in sum
start = time.clock()
sum(arr)            # Python内部函数sum通过数组a的迭代接口访问其每个元素，因此速度很慢
print("python_sum:", time.clock() - start)

# 终端输出
# (' weave_sum:', 0.011916870000000001)
# (' numpy_sum:', 0.011501299999999999)
# ('python_sum:', 4.23033)