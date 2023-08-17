import numpy as np

t = np.linspace(0, 30, 101)
data_array = np.random.rand(101, 2)  # 示例数据数组

result = []

for time_value in t:
    # 创建一个全为 time_value 的列向量
    time_column = np.full((101, 1), time_value)
    
    # 拼接时间列和 data_array
    new_data = np.hstack((data_array, time_column))
    
    result.append(new_data)

# 现在，result 是一个列表，其中包含 101 个 (101, 3) 的数组。

print(result)