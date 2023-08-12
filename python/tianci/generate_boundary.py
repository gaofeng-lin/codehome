import numpy as np

boundary_samples = 3

# 在[-π, π]范围内随机均匀采样
samples_x = np.random.uniform(-np.pi, np.pi, boundary_samples)
samples_y = np.random.uniform(-np.pi, np.pi, boundary_samples)

# 构造符合条件的边界点
x_boundary = np.concatenate([samples_x, samples_x, -np.pi*np.ones_like(samples_y), np.pi*np.ones_like(samples_y)])
y_boundary = np.concatenate([-np.pi*np.ones_like(samples_x), np.pi*np.ones_like(samples_x), samples_y, samples_y])

boundary_inputs = np.stack([x_boundary, y_boundary], axis=-1)

print(boundary_inputs)
