import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the data from the txt file
data = np.loadtxt('C:\\Users\\76585\\Desktop\\天池结果文件v2\\lossfile\\Based_BasedTrueDataloss_AbslossPdeloss_Use15630Point_UseAllData_Alldata.txt', delimiter=' ')  # assuming data is separated by tabs

iterations = data[:, 0]
train_loss = data[:, 1]
# pde_mse_loss = data[:, 2]
# conservation_mse_loss = data[:, 3]
data_mre_loss = data[:, 2]

train_mre_loss = data[:, 3]
ux_mre_loss = data[:, 4]
uy_mre_loss = data[:, 5]
p_mre_loss = data[:, 6]

ux_subtraction_mre_loss = data[:, 7]
uy_subtraction_mre_loss = data[:, 8]
p_subtraction_mre_loss = data[:, 9]

fake_data_loss = data[:, 4]
boundry_loss = data[:, 5]
conservation_loss = data[:, 6]
# train_loss = pde_loss + data_loss

# 寻找各loss的最大值和最小值及其对应的迭代次数
train_min_idx = np.argmin(train_loss)
train_max_idx = np.argmax(train_loss)
train_mre_loss_min_idx = np.argmin(train_mre_loss)
# pde_min_idx = np.argmin(pde_loss)
# pde_max_idx = np.argmax(pde_loss)
# data_min_idx = np.argmin(data_loss)
# data_max_idx = np.argmax(data_loss)

# 绘制三种loss
plt.figure(figsize=(10, 6))
plt.plot(iterations, train_loss, label='Train Loss', color='b')
# plt.plot(iterations, pde_mse_loss, label='Pde Mse Loss', color='#122856')
# plt.plot(iterations, conservation_mse_loss, label='Conservation Mse Loss', color='#535612')
plt.plot(iterations, data_mre_loss, label='Data Mre Loss', color='r')
plt.plot(iterations, train_mre_loss, label='Train Mre Loss', color='g')
plt.plot(iterations, ux_mre_loss, label='Ux Mre Loss', color='k')
plt.plot(iterations, uy_mre_loss, label='Uy Mre Loss', color='y')
plt.plot(iterations, p_mre_loss, label='P Mre Loss', color='c')
plt.plot(iterations, ux_subtraction_mre_loss, label='Ux Subtraction Mre Loss', color='#564912')
plt.plot(iterations, uy_subtraction_mre_loss, label='Uy Subtraction Mre Loss', color='#125636')
plt.plot(iterations, p_subtraction_mre_loss, label='P Subtraction Mre Loss', color='#501256')

# 在图上标注各loss的最大值和最小值
plt.annotate(f"Min: {train_loss[train_min_idx]:.5f}", (iterations[train_min_idx], train_loss[train_min_idx]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.annotate(f"Min: {train_mre_loss[train_mre_loss_min_idx]:.5f}", (iterations[train_mre_loss_min_idx], train_mre_loss[train_mre_loss_min_idx]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
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