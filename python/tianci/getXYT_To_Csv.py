import numpy as np
import pandas as pd

# 这个代码是将512*512的xyt保存为csv文件

# 定义数据
t = np.linspace(0,30,101)
nn = 512 * 512
d = 2*np.pi/512
x = np.linspace(-np.pi, np.pi-d, 512)
y = np.linspace(-np.pi, np.pi-d, 512)

# 使用meshgrid来获取所有的x, y和t组合
X, Y, T = np.meshgrid(x, y, t)
print(X.shape)

# 将这些组合变成所需的形状
XYT = np.stack((X.ravel(), Y.ravel(), T.ravel()), axis=-1)
print(XYT.shape)
# 使用pandas将结果保存为CSV文件
df = pd.DataFrame(XYT, columns=['x', 'y', 't'])
df.to_csv('C:\\Users\\76585\\Desktop\\512_xyt_coordinates.csv', index=False)


