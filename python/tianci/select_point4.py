import h5py
import numpy as np

# 这个文件的主要目的是检验新生成的select_64_point.h5是否能正常读取

f = h5py.File('C:\\Users\\76585\\Desktop\\select_point\\select_64_point.h5', 'r')
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

# 接下来我要组装数据，data 是一个形状为 (101, 64, 64, 3) 的数组，包含 ux, uy, p 的值。
# 重塑y['data']来达到期望的形状
# combined = y['data'].reshape((101, 64, 64, 3))


# 这样，combined就是一个形状为(101, 64, 64, 6)的数组
# 如果你确实需要结果为(101, 64, 64, 3)，你可以在拼接之前选择所需的列
print('XYT shape is: ', XYT.shape)
print('y data shape is: ', y['data'].shape)



