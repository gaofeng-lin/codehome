# 这段代码是从原始数据当中把值小于-e4的数据选出来，按照ux,uy,p分类。

import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay, distance
from collections import defaultdict
from shapely.geometry import Polygon, Point, LineString
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

r_ux = np.hstack((truth_xyt, truth_data[:, 0].reshape(-1,1)))



r_uy = np.hstack((truth_xyt, truth_data[:, 1].reshape(-1,1)))
r_p = np.hstack((truth_xyt, truth_data[:, 2].reshape(-1,1)))

r_ux = FilteredData(r_ux)
r_uy = FilteredData(r_uy)
p = FilteredData(r_p)

print('r_ux shape: ', r_ux)

data = p
unique_t_values = np.unique(data[:, 2])

# PlotData(p)


pres = np.load('C:\\Users\\76585\\Desktop\\天池结果文件v2\\data\\pres.npy')
pres = pres.reshape(-1, 1)
# 定义数据
t = np.linspace(0,30,101)
nn = 512 * 512
d = 2*np.pi/512
x = np.linspace(-np.pi, np.pi-d, 512)
y = np.linspace(-np.pi, np.pi-d, 512)

# 使用meshgrid来获取所有的x, y和t组合
X, Y, T = np.meshgrid(x, y, t)
print(X.shape)

# 将这些组合变成所需的形状
XYT = np.stack((X.ravel(), Y.ravel(), T.ravel()), axis=-1)

data2 = np.hstack((XYT, pres))
# data2 = np.random.random((100,4))
data2 = data2[:1000000,:]

print(data2.shape)





# PlotData(p)



def plot_edges_below_threshold(tri, threshold=0.44):
    for simplex in tri.simplices:
        for i in range(3):
            u, v = sorted([simplex[i], simplex[(i+1)%3]])
            dist = distance.euclidean(tri.points[u], tri.points[v])
            if dist <= threshold:
                plt.plot([tri.points[u][0], tri.points[v][0]],
                         [tri.points[u][1], tri.points[v][1]], 'k-')

def plot_rectangles_below_threshold(tri, threshold=0.44, width=0.075):
    for simplex in tri.simplices:
        for i in range(3):
            u, v = sorted([simplex[i], simplex[(i+1)%3]])
            dist = distance.euclidean(tri.points[u], tri.points[v])
            if dist <= threshold:
                dx = tri.points[v][0] - tri.points[u][0]
                dy = tri.points[v][1] - tri.points[u][1]
                angle = np.arctan2(dy, dx)
                
                # 计算矩形的中心点坐标
                center_x = (tri.points[u][0] + tri.points[v][0]) / 2
                center_y = (tri.points[u][1] + tri.points[v][1]) / 2
                
                # 根据连线方向调整矩形的方向和坐标
                if abs(dx) > abs(dy):
                    p1 = (center_x - dist / 2, center_y - width / 2)
                    p2 = (center_x + dist / 2, center_y - width / 2)
                    p3 = (center_x + dist / 2, center_y + width / 2)
                    p4 = (center_x - dist / 2, center_y + width / 2)
                else:
                    p1 = (center_x - width / 2, center_y - dist / 2)
                    p2 = (center_x + width / 2, center_y - dist / 2)
                    p3 = (center_x + width / 2, center_y + dist / 2)
                    p4 = (center_x - width / 2, center_y + dist / 2)
                
                rectangle = plt.Polygon([p1, p2, p3, p4], edgecolor='red', fill=False)
                plt.gca().add_patch(rectangle)

for t in unique_t_values:
    subset = data[data[:, 2] == t]
    tri = Delaunay(subset[:, :2])
    
    plt.figure(figsize=(10, 8))
    plt.scatter(subset[:, 0], subset[:, 1], c=subset[:, 3], cmap='viridis')  # 使用p值为颜色
    plot_rectangles_below_threshold(tri, width=0.075)
    
    plt.colorbar(label='p value')
    plt.title(f"Data for t={t}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

