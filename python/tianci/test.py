# 这个代码是取出一个时间切片，然后看看在x

import numpy as np

n = 512
bin_width = 2*np.pi/n
x = np.linspace(-np.pi+bin_width/2, np.pi-bin_width/2, 512)
y = np.linspace(np.pi-bin_width/2, -np.pi+bin_width/2, 512)
X, Y = np.meshgrid(x, y)
X = np.array(X.flatten())
Y = np.array(Y.flatten())
print('X: ',X)
print("Y: " ,Y)

# for i in range(0, 512*512):
#     XY = np.array([X[i], Y[i]])
#     # print(XY)
#     print(XY)
#     breakpoint