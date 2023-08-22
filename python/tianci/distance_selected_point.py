import numpy as np

d = 2 * np.pi / 512
x = np.linspace(-np.pi, np.pi - d, 512)
y = np.linspace(-np.pi, np.pi - d, 512)
nn = 512 * 512

# 创建一个坐标矩阵
coordinates = [[xi, yi] for xi in x for yi in y]

# 给定的坐标点
# given_point = np.array([2.932971, 2.147573])
# 
given_point = np.array([2.147573, 1.754874])

# given_point = np.array([0.969476, -1.38672])
# 计算给定坐标点与所有 coordinates 点的距离
distances = np.linalg.norm(coordinates - given_point, axis=1)

# 设置距离阈值
distance_threshold = 0.15

# 找到在距离阈值范围内的点的索引
close_points_indices = np.where(distances <= distance_threshold)

# 输出找到的坐标点及其索引
count = 0
for idx in close_points_indices[0]:
    count += 1
    # print(f"Coordinate: {coordinates[idx]}, Index: {idx}")

print('count is: ', count)