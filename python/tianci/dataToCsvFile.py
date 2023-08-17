import pandas as pd
import h5py
import numpy as np
# 从h5文件中将数据提取出来，保存为csv格式



# 创建一个DataFrame

def generate(filepath):
    f = h5py.File(filepath, 'r')
    XYT = np.zeros((0,3))
    UX = np.zeros((0,1))
    UY = np.zeros((0,1))
    P = np.zeros((0,1))
    for key in f.keys():
        time = float(key)
        print('time is : ', time)
        XY = f[key][:,0:2]
        ux = f[key][:,2]
        print('ux is :', ux)
        uy = f[key][:,3][:,None]
        p = f[key][:,4][:,None]
        XYT = np.concatenate((XYT, np.concatenate((XY, np.full((XY.shape[0],1), time)), axis=1)), axis=0)
        UX = np.concatenate((UX, ux), axis=0)
        UY = np.concatenate((UY, uy), axis=0)
        P = np.concatenate((P, p), axis=0)
    X, y = {}, {}
    X['data'] = XYT
    y['data'] = np.concatenate((UX, UY, P), axis=1)

    frame_data = np.hstack((XYT, y['data']))

    return frame_data

frame_data = np.load("C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\selected_data.npy")

# frame_data = generate("C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\data_extension.h5")

breakpoint()
x = frame_data[:,0]
y = frame_data[:,1]
t = frame_data[:,2]
ux = frame_data[:,3]
uy = frame_data[:,4]
p = frame_data[:,5]

print(ux)

df = pd.DataFrame({
    'x': x,
    'y': y,
    't': t,
    'ux': ux,
    'uy': uy,
    'p': p
})

# 将DataFrame写入CSV文件
df.to_csv('C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\selected_data.csv', index=False)
