import numpy as np
import matplotlib.pyplot as plt
#  画出16*16和512*512的xyt

d = 2*np.pi/512
x = np.linspace(-np.pi, np.pi-d, 512)
y = np.linspace(-np.pi, np.pi-d, 512)
nn = 512 * 512

# 创建一个坐标矩阵
coordinates = [[xi, yi] for xi in x for yi in y]

X_values = []
Y_values = []

for i in range(nn):
    X = coordinates[i][0]
    Y = coordinates[i][1]
    X_values.append(X)
    Y_values.append(Y)

# 绘制坐标点的散点图
plt.figure(figsize=(8, 8))
plt.scatter(X_values, Y_values, s=1, c='b', marker='.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Coordinates')
plt.grid(True)
plt.show()