import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay, distance
from collections import defaultdict
from shapely.geometry import Polygon, Point, LineString
from scipy.spatial.distance import euclidean
from matplotlib.patches import Rectangle
# import shapely


def PlotData(data):
    unique_t_values = np.unique(data[:, 2])

    for t in unique_t_values:
        subset = data[data[:, 2] == t]

        x = subset[:, 0]
        y = subset[:, 1]
        p = subset[:, 3]

        plt.figure()
        plt.scatter(x, y, c=p, cmap='viridis')  # 使用p值为颜色
        plt.colorbar(label='p value')
        plt.title(f"Data for t={t}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


def FilteredData(data):
    filtered_data = data[ (data[:, 3] > -9e-4) & (data[:, 3] < 0)]
    return filtered_data

def generate():
    # f = h5py.File('./Data_16.h5', 'r')
    f = h5py.File('C:\\Competition\\baseline_v2\\data_16.h5', 'r')
    n_frame = len(f.keys())
    XYT = np.zeros((0,3))
    UX = np.zeros((0,1))
    UY = np.zeros((0,1))
    P = np.zeros((0,1))
    for key in f.keys():
        time = float(key)
        XY = f[key][:,0:2]
        ux = f[key][:,2][:,None]
        uy = f[key][:,3][:,None]
        p = f[key][:,4][:,None]
        XYT = np.concatenate((XYT, np.concatenate((XY, np.full((XY.shape[0],1), time)), axis=1)), axis=0)
        UX = np.concatenate((UX, ux), axis=0)
        UY = np.concatenate((UY, uy), axis=0)
        P = np.concatenate((P, p), axis=0)
    X, y = {}, {}
    X['data'] = XYT
    y['data'] = np.concatenate((UX, UY, P), axis=1)
    return X, y




X, y = generate()
truth_xyt = X['data']
truth_data = y['data']

print(truth_xyt[:256,0:2])

points = truth_xyt[:256,0:2]

print(points)

breakpoint()

# 提取x坐标和y坐标
x_coords = points[:, 0]
y_coords = points[:, 1]

# 绘制坐标图
plt.scatter(x_coords, y_coords, color='blue', label='Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Coordinate Plot')
plt.grid(True)
plt.legend()

# 随机选择一个除边界点外的中间点索引
middle_indices = list(range(1, len(points) - 1))  # 排除第一个和最后一个点
random_index = np.random.choice(middle_indices)

# 获取基准点的坐标
random_point = points[random_index]

# 获取水平相邻点的索引
horizontal_neighboring_index = (random_index + 1) % len(points)

# 获取垂直相邻点的索引
vertical_neighboring_index = (random_index + len(points) // 2) % len(points)

# 获取水平相邻点和垂直相邻点的坐标
horizontal_neighboring_point = points[horizontal_neighboring_index]
vertical_neighboring_point = points[vertical_neighboring_index]

# 计算与水平相邻点的距离
horizontal_distance = np.linalg.norm(horizontal_neighboring_point - random_point)

# 计算与垂直相邻点的距离
vertical_distance = np.linalg.norm(vertical_neighboring_point - random_point)

print("Random Point:", random_point)
print("Horizontal Neighboring Point:", horizontal_neighboring_point)
print("Vertical Neighboring Point:", vertical_neighboring_point)
print("Distance to Horizontal Neighboring Point:", horizontal_distance)
print("Distance to Vertical Neighboring Point:", vertical_distance)

# 显示图形
plt.show()