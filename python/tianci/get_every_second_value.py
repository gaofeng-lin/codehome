import numpy as np

def get_every_second_value(start, stop, num):
    """
    从start到stop生成num个数据，然后获取每两个相邻数据之间的一个数据，返回一个包含这些数据的NumPy数组。
    
    参数：
    start (float)：起始值。
    stop (float)：结束值。
    num (int)：生成数据的数量。

    返回：
    numpy.ndarray：包含每两个相邻数据之间的一个数据的数组。
    """
    t = np.linspace(start, stop, num)
    new_t = t[1::2]
    return new_t

# 使用示例
start = 0
stop = 30
num = 101
# result = get_every_second_value(start, stop, num)
# print(result)

t = np.linspace(0,30,101)
print(t)





# 创建原始列表 t，包含5个数据


# 计算每两个相邻值的平均值
new_t = (t[:-1] + t[1:]) / 2

# 打印新的列表
print(len(new_t))
