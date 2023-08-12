import h5py
import numpy as np
# 这个代码是从64*64的h5文中选取满足控制方程的点 

f = h5py.File('C:\\Users\\76585\\Desktop\\select_point\\Prediction_store_64.h5', 'r')
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
combined = y['data'].reshape((101, 64, 64, 3))


# 这样，combined就是一个形状为(101, 64, 64, 6)的数组
# 如果你确实需要结果为(101, 64, 64, 3)，你可以在拼接之前选择所需的列
print('combined shape is: ', combined.shape)

data = combined

# 假设 data 是一个形状为 (101, 64, 64, 3) 的数组，包含 ux, uy, p 的值。

delta_space = 2*np.pi/64
delta_time = 30/100  # 0 to 30 over 101 frames

def compute_spatial_derivatives(data, frame_index, i, j, delta_space):
    ux_x = (data[frame_index, i+1, j, 0] - data[frame_index, i-1, j, 0]) / (2 * delta_space)
    ux_y = (data[frame_index, i, j+1, 0] - data[frame_index, i, j-1, 0]) / (2 * delta_space)
    uy_x = (data[frame_index, i+1, j, 1] - data[frame_index, i-1, j, 1]) / (2 * delta_space)
    uy_y = (data[frame_index, i, j+1, 1] - data[frame_index, i, j-1, 1]) / (2 * delta_space)
    p_x = (data[frame_index, i+1, j, 2] - data[frame_index, i-1, j, 2]) / (2 * delta_space)
    p_y = (data[frame_index, i, j+1, 2] - data[frame_index, i, j-1, 2]) / (2 * delta_space)

    # 二阶导数
    ux_xx = (data[frame_index, i+1, j, 0] - 2*data[frame_index, i, j, 0] + data[frame_index, i-1, j, 0]) / (delta_space**2)
    ux_yy = (data[frame_index, i, j+1, 0] - 2*data[frame_index, i, j, 0] + data[frame_index, i, j-1, 0]) / (delta_space**2)
    uy_xx = (data[frame_index, i+1, j, 1] - 2*data[frame_index, i, j, 1] + data[frame_index, i-1, j, 1]) / (delta_space**2)
    uy_yy = (data[frame_index, i, j+1, 1] - 2*data[frame_index, i, j, 1] + data[frame_index, i, j-1, 1]) / (delta_space**2)

    return ux_x, ux_y, uy_x, uy_y, p_x, p_y, ux_xx, ux_yy, uy_xx, uy_yy


MSE_total = np.zeros((101, 64, 64))

count = 0

for frame_index in range(101):
    for i in range(1, 63):  # Skipping the first and last points in space
        for j in range(1, 63):
            
            # 获取 ux, uy, p 的值
            ux = data[frame_index, i, j, 0]
            uy = data[frame_index, i, j, 1]
            p = data[frame_index, i, j, 2]
            
            # 计算时间导数
            if frame_index == 0:  # First frame
                ux_t = (data[frame_index + 1, i, j, 0] - data[frame_index, i, j, 0]) / delta_time
                uy_t = (data[frame_index + 1, i, j, 1] - data[frame_index, i, j, 1]) / delta_time
            elif frame_index == 100:  # Last frame
                ux_t = (data[frame_index, i, j, 0] - data[frame_index - 1, i, j, 0]) / delta_time
                uy_t = (data[frame_index, i, j, 1] - data[frame_index - 1, i, j, 1]) / delta_time
            else:  # Middle frames
                ux_t = (data[frame_index + 1, i, j, 0] - data[frame_index - 1, i, j, 0]) / (2 * delta_time)
                uy_t = (data[frame_index + 1, i, j, 1] - data[frame_index - 1, i, j, 1]) / (2 * delta_time)
            
            # 计算空间导数
            ux_x, ux_y, uy_x, uy_y, p_x, p_y, ux_xx, ux_yy, uy_xx, uy_yy = compute_spatial_derivatives(data, frame_index, i, j, delta_space)
            
            # 控制方程的残差
            fx = 0.025 * np.sin(2*i*delta_space) * np.cos(2*j*delta_space)
            fy = -0.025 * np.cos(2*i*delta_space) * np.sin(2*j*delta_space)
            
            MSEr1 = (ux_t + ux*ux_x + uy*ux_y + p_x - 4.66e-4*(ux_xx + ux_yy) - fx)**2
            MSEr2 = (uy_t + ux*uy_x + uy*uy_y + p_y - 4.66e-4*(uy_xx + uy_yy) - fy)**2
            MSEr3 = (ux_x + uy_y)**2
            
            # MSE_total[frame_index, i, j] = MSEr1 + MSEr2 + MSEr3
            MSE_total = (MSEr1 + MSEr2 + MSEr3)/3

            if MSE_total < 4e-5:
                x, y, t = i*delta_space, j*delta_space, frame_index*delta_time
                ux, uy, p = data[frame_index, i, j, 0], data[frame_index, i, j, 1], data[frame_index, i, j, 2]
                print(f"x: {x}, y: {y}, t: {t}, ux: {ux}, uy: {uy}, p: {p}")
                count = count + 1
# print(MSE_total[4,,54])
print("count is : ", count)

