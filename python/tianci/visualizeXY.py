import numpy as np
import h5py
import matplotlib.pyplot as plt
# 这个代码是可视化h5文件中x,y在二维平面上的坐标分布

def generate(num):
    f = h5py.File('C:\\Users\\76585\\Desktop\\select_point\\data_16_v2.h5', 'r')
    #n_frame = len(f.keys())
    tlist = ["012.6", "012.9", "013.2", "013.5"]
    n_frame = len(f.keys())
    # n_frame = len(tlist)
    XYT = np.zeros((0,3))
    UX = np.zeros((0,1))
    UY = np.zeros((0,1))
    P = np.zeros((0,1))
    for key in f.keys():
    # for key in tlist:
        time = float(key)
        XY = f[key][:,0:2]
        ux = f[key][:,2][:,None]
        uy = f[key][:,3][:,None]
        p  = f[key][:,4][:,None]
        XYT = np.concatenate((XYT, np.concatenate((XY, np.full((XY.shape[0],1), time)), axis=1)), axis=0)
        UX  = np.concatenate((UX, ux), axis=0)
        UY  = np.concatenate((UY, uy), axis=0)
        P   = np.concatenate((P, p), axis=0)
    X, y = {}, {}
    randXY = np.random.rand(10*n_frame, 2)*2*np.pi-np.pi
    randT = np.random.rand(10*n_frame, 1) * (float(tlist[-1]) - float(tlist[0])) + float(tlist[0])
    X['pde'] = np.concatenate((randXY, randT), axis=1)
    X['data'] = XYT
    np.savetxt("aaa.data", X['pde'])
    plt.scatter(X['data'][:,0], X['data'][:,1])
    plt.show()
    plt.scatter(X['data'][:,1], X['data'][:,2])
    plt.show()
    y['data'] = np.concatenate((UX, UY, P), axis=1)
    return X, y

X, y = generate(10)
print("X[data] shape: ", X['data'].shape)
print("y[data] shape: ", y['data'].shape)