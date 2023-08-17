import pandas as pd
import h5py
import numpy as np
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
        ux = f[key][:,2][:,None]
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

frame_data = generate("C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\data_16_v2.h5")