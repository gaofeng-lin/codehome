import numpy as np

# 原始数组
original_array = np.random.random((100, 6))

# 随机选择的行数
num_rows = 20

# 随机选择行的索引
random_indices = np.random.choice(original_array.shape[0], size=num_rows, replace=False)

# 根据索引获取随机选择的行
selected_rows = original_array[random_indices]

# 打印结果
print(selected_rows)
