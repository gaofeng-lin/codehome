import numpy as np

# 假设您有 origin 和 predict 数组
origin = np.random.rand(16*16*101, 6)
predict = np.random.rand(512*512*101, 6)



# 创建一个对应关系的数组
correspondence = np.empty((16*16*101, 1024), dtype=int)
for i in range(16*16*101):
    correspondence[i] = np.arange(i*1024, (i+1)*1024)

# 修改 predict 数组中对应的值
condition = origin[:, 3] < -1e-5  # 根据 ux 的条件
predict[correspondence[condition, :], 3] *= 1e-3

condition = origin[:, 4] < -1e-5  # 根据 uy 的条件
predict[correspondence[condition, :], 4] *= 1e-3

condition = origin[:, 5] < -1e-5  # 根据 p 的条件
predict[correspondence[condition, :], 5] *= 1e-3
