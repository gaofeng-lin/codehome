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
i=0

# 取256行数据，如果不足256行，则取所有剩余的行
end_idx = min(i+256, xy.shape[0])

# 提取 x, y, z 坐标
x = xy[i:end_idx, 0]
y = xy[i:end_idx, 1]
z = uy[i:end_idx, 0]

x_min, x_max = np.amin(xy[:, 0]), np.amax(xy[:, 0])
y_min, y_max = np.amin(xy[:, 1]), np.amax(xy[:, 1])

print("X range: ", (x_min, x_max))
print("Y range: ", (y_min, y_max))

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.scatter(xy[:, 0], xy[:, 1], c='blue')
plt.xlim(-np.pi, np.pi)
plt.ylim(-np.pi, np.pi)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot of X and Y coordinates')
plt.grid(True)
plt.show()

