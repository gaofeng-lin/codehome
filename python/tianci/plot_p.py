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




for i in range(0, xy.shape[0], 256):
    # 取256行数据，如果不足256行，则取所有剩余的行
    end_idx = min(i+256, xy.shape[0])
    
    # 提取 x, y, z 坐标
    x = xy[i:end_idx, 0]
    y = xy[i:end_idx, 1]
    z = p[i:end_idx, 0]

    # 找出最大值和最小值
    # zmin = np.min(z)
    # zmax = np.max(z)

    # 绘制散点图
    ax.scatter(x, y, z, marker='o')

    # 将最大值和最小值添加到图中
    # ax.text(x[0], y[0], zmax, "Max Z: %.2f" % zmax, color='red')
    # ax.text(x[0], y[0], zmin, "Min Z: %.2f" % zmin, color='blue')

    # 更新最大值和最小值
    zmin = min(zmin, np.min(z))
    zmax = max(zmax, np.max(z))

# 设置轴的标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('p')
plt.title('3D Scatter Plot\nMin p: %.2f, Max p: %.2f' % (zmin, zmax))

# 展示图形
plt.show()

