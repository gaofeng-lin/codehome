import numpy as np

n = 4
bin_width = 2*np.pi/n
x = np.linspace(-np.pi+bin_width/2, np.pi-bin_width/2, n)
y = np.linspace(np.pi-bin_width/2, -np.pi+bin_width/2, n)
X, Y = np.meshgrid(x, y)

# 按照指定的顺序提取边界上的点
# 1. (x, -pi)
boundary_x1 = X[Y==y[-1]]
boundary_y1 = Y[Y==y[-1]]

# 2. (x, pi)
boundary_x2 = X[Y==y[0]]
boundary_y2 = Y[Y==y[0]]

# 3. (-pi, y)
boundary_x3 = X[X==x[0]]
boundary_y3 = Y[X==x[0]]

# 4. (pi, y)
boundary_x4 = X[X==x[-1]]
boundary_y4 = Y[X==x[-1]]

# 按顺序连接各边界点
boundary_x = np.concatenate((boundary_x1, boundary_x2, boundary_x3, boundary_x4))
boundary_y = np.concatenate((boundary_y1, boundary_y2, boundary_y3, boundary_y4))

# 打印挑选出的点
count = 0
for ix, iy in zip(boundary_x, boundary_y):
    print(ix, iy)
    count = count +1

b = np.stack([boundary_x, boundary_y], axis= -1)

c = np.repeat(b, repeats=101, axis=0)

print(c)
