import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate(num):
    # f = h5py.File('./Data_16.h5', 'r')
    f = h5py.File('C:\\Users\\76585\\Desktop\\tianchi\\data_16.h5', 'r')
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
    randXY = np.random.rand(num['pde']*n_frame, 2)*2*np.pi-np.pi
    randT = np.random.rand(num['pde']*n_frame, 1) * 30
    X['pde'] = np.concatenate((randXY, randT), axis=1)
    X['data'] = XYT
    y['data'] = np.concatenate((UX, UY, P), axis=1)
    return X, y


train_num = {'pde': 1024}

X, y = generate(train_num)
truth_xyt = X['data']
# print('truch_xyt shape: ', truth_xyt.shape)

ux = y['data'][:,0:1]
uy = y['data'][:,1:2]
p = y['data'][:,2:3]

xy = truth_xyt[:, 0:2]

# print('ux shape :', xy.shape)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 初始化最大值和最小值
zmin = np.inf
zmax = -np.inf
zmax_idx = None

i = 86

# 取256行数据，如果不足256行，则取所有剩余的行
end_idx = min(i+256, xy.shape[0])

# 提取 x, y, z 坐标
x = xy[i:end_idx, 0]
y = xy[i:end_idx, 1]
z = ux[i:end_idx, 0]

# 创建空的字典来保存找到的点
x_pi_points = {}
x_minus_pi_points = {}
y_pi_points = {}
y_minus_pi_points = {}

# 搜索满足条件的点
for i in range(xy.shape[0]):
    x_val = xy[i, 0]
    y_val = xy[i, 1]
    z_val = ux[i, 0]

    # 如果x值接近-pi或pi，则保存点的y值和z值
    if np.isclose(x_val, -np.pi):
        x_minus_pi_points[y_val] = (x_val, y_val, z_val)
    elif np.isclose(x_val, np.pi):
        x_pi_points[y_val] = (x_val, y_val, z_val)

    # 如果y值接近-pi或pi，则保存点的x值和z值
    if np.isclose(y_val, -np.pi):
        y_minus_pi_points[x_val] = (x_val, y_val, z_val)
    elif np.isclose(y_val, np.pi):
        y_pi_points[x_val] = (x_val, y_val, z_val)

# 找到匹配的点对并打印
def print_matching_pairs(dict1, dict2):
    for key in dict1:
        if key in dict2:
            print("Matching pair: ", dict1[key], dict2[key])

print("Matching pairs for x=-pi and x=pi:")
print_matching_pairs(x_minus_pi_points, x_pi_points)
print("Matching pairs for y=-pi and y=pi:")
print_matching_pairs(y_minus_pi_points, y_pi_points)
