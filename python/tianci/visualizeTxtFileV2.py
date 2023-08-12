import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the data from the txt file
data = np.loadtxt('C:\\Users\\76585\\Desktop\\天池结果文件\\lossfile\\dataLossChangeMre.txt', delimiter=' ')  # assuming data is separated by tabs

iterations = data[:, 0]
train_loss = data[:, 1]
# pde_loss = data[:, 2]
data_mre_loss = data[:, 2]

train_mre_loss = data[:, 3]
ux_mre_loss = data[:, 4]
uy_mre_loss = data[:, 5]
p_mre_loss = data[:, 6]

# fake_data_loss = data[:, 4]
# boundry_loss = data[:, 5]
# conservation_loss = data[:, 6]
# train_loss = pde_loss + data_loss

# 寻找各loss的最大值和最小值及其对应的迭代次数
train_min_idx = np.argmin(train_loss)
train_max_idx = np.argmax(train_loss)
# pde_min_idx = np.argmin(pde_loss)
# pde_max_idx = np.argmax(pde_loss)
# data_min_idx = np.argmin(data_loss)
# data_max_idx = np.argmax(data_loss)

# 绘制三种loss
plt.figure(figsize=(10, 6))
plt.plot(iterations, train_loss, label='Train Loss', color='b')
plt.plot(iterations, data_mre_loss, label='Data MRE Loss', color='r')
plt.plot(iterations, train_mre_loss, label='Train Mre Loss', color='g')
plt.plot(iterations, ux_mre_loss, label='Ux Mrse Loss', color='k')
plt.plot(iterations, uy_mre_loss, label='Uy Mrse Loss', color='y')
plt.plot(iterations, p_mre_loss, label='P Mrse Loss', color='c')

# 在图上标注各loss的最大值和最小值
plt.annotate(f"Min: {train_loss[train_min_idx]:.5f}", (iterations[train_min_idx], train_loss[train_min_idx]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
# plt.annotate(f"Max: {train_loss[train_max_idx]:.2f}", (iterations[train_max_idx], train_loss[train_max_idx]), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=8)

# plt.annotate(f"Min: {pde_loss[pde_min_idx]:.2f}", (iterations[pde_min_idx], pde_loss[pde_min_idx]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
# plt.annotate(f"Max: {pde_loss[pde_max_idx]:.2f}", (iterations[pde_max_idx], pde_loss[pde_max_idx]), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=8)

# plt.annotate(f"Min: {data_loss[data_min_idx]:.2f}", (iterations[data_min_idx], data_loss[data_min_idx]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
# plt.annotate(f"Max: {data_loss[data_max_idx]:.2f}", (iterations[data_max_idx], data_loss[data_max_idx]), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=8)

plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Loss Value')
plt.title('Loss Trends over Iterations')
plt.grid(True)
plt.tight_layout()
plt.show()