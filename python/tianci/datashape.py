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

random_xyt = X['pde']
print('truth_xyt shape: ', truth_xyt)

