# 这段代码是针对实验32，但是对内存要求比较高，具体的运行是放到服务器上面的

import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from scipy.spatial import Delaunay, distance
from collections import defaultdict
from shapely.geometry import Polygon, Point, LineString
# from scipy.spatial.distance import euclidean
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

r_ux = np.hstack((truth_xyt, truth_data[:, 0].reshape(-1,1)))



r_uy = np.hstack((truth_xyt, truth_data[:, 1].reshape(-1,1)))
r_p = np.hstack((truth_xyt, truth_data[:, 2].reshape(-1,1)))

r_ux = FilteredData(r_ux)
r_uy = FilteredData(r_uy)
p = FilteredData(r_p)



data = p
unique_t_values = np.unique(data[:, 2])

# PlotData(p)


pres = np.load('C:\\Users\\76585\\Desktop\\天池结果文件v2\\data\\pres.npy')
pres = pres.reshape(-1, 1)

data2 = np.load('C:\\Users\\76585\\Desktop\\天池结果文件v2\\data\\data2.npy')





# data2 = data2[:1000000,:]







# PlotData(p)


def plot_rectangles_below_threshold(subset, threshold=0.44, width=0.075):
    all_value = []
    count = 0
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            point1 = subset[i, :2]
            point2 = subset[j, :2]
            dist = np.linalg.norm(point2 - point1)
            
            if dist <= threshold:
                dx = point2[0] - point1[0]
                dy = point2[1] - point1[1]
                angle = np.arctan2(dy, dx)
                
                # 计算矩形的中心点坐标
                center_x = (point1[0] + point2[0]) / 2
                center_y = (point1[1] + point2[1]) / 2
                
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
                
                value = []
                value.append(p1)
                value.append(p2)
                value.append(p3)
                value.append(p4)
                # rectangle = plt.Polygon([p1, p2, p3, p4], edgecolor='red', fill=False)
                # print('value: ', value)
                all_value.append(value)
         
                # plt.gca().add_patch(rectangle)

    return all_value
rectangle_dict = {}


t_list = []
for t in unique_t_values:
    subset = data[data[:, 2] == t]
    
    has_rectangles = False
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            point1 = subset[i, :2]
            point2 = subset[j, :2]
            dist = np.linalg.norm(point2 - point1)
            if dist <= 0.44:
                has_rectangles = True
                break
    
    if has_rectangles:
    
        rectangle = plot_rectangles_below_threshold(subset, width=0.075)
        # rectangle.append(t)
        t_list.append(t)
        rectangle_dict[t] = rectangle

# t_list有28个
# print("rectangle_dict: ", rectangle_dict)



# filtered_data = data2[np.isin(data2[:, 2], t_list)]

# print(filtered_data.shape)

# 创建一个哈希表，用于存储每个t时刻对应的矩阵的Polygon对象
polygon_dict = {}
for t, rectangles in rectangle_dict.items():
    polygons = [Polygon(rectangle) for rectangle in rectangles]
    polygon_dict[t] = polygons

filtered_data = data2[np.isin(data2[:, 2], t_list)]

print('开始修改')

# 创建一个字典来记录每个t时刻在filtered_data中的索引
t_indices = defaultdict(list)
for i, row in enumerate(filtered_data):
    t_indices[row[2]].append(i)

# 遍历筛选后的数据进行修改，并记录需要替换的索引
indices_to_replace = []
for i, row in enumerate(filtered_data):
    x, y, current_t, p = row
    if current_t in polygon_dict:
        polygons = polygon_dict[current_t]
        point = Point(x, y)
        for polygon in polygons:
            if polygon.contains(point):
                p *= 1e-3
                filtered_data[i, 3] = p
                indices_to_replace.extend(t_indices[current_t])
                break
print('修改完成')

# 将修改后的数据替换回原始data2中相应的位置
data2[indices_to_replace] = filtered_data

print('data2 shape is: ', data2.shape)