import matplotlib.pyplot as plt
import re

# 日志文件路径
log_file_path = 'C:/Users/76585/Desktop/logfile/simvp/68.log'

# 初始化用于存储epoch数、训练集loss和验证集loss的列表
epochs, train_losses, val_losses = [], [], []

# 读取日志文件
with open(log_file_path, 'r') as file:
    for line in file:
        # 使用正则表达式匹配每行中的epoch和loss值
        match = re.search(r'Epoch: (\d+) \| Train Loss: ([\d.]+) Vali Loss: ([\d.]+)', line)
        if match:
            epochs.append(int(match.group(1)))
            train_losses.append(float(match.group(2)))
            val_losses.append(float(match.group(3)))

# 找出训练集和验证集loss的极小值
min_train_loss = min(train_losses)
min_train_epoch = epochs[train_losses.index(min_train_loss)]
min_val_loss = min(val_losses)
min_val_epoch = epochs[val_losses.index(min_val_loss)]

# 找出训练集和验证集loss的极大值
max_train_loss = max(train_losses)
max_train_epoch = epochs[train_losses.index(max_train_loss)]
max_val_loss = max(val_losses)
max_val_epoch = epochs[val_losses.index(max_val_loss)]

# 绘图
plt.figure(figsize=(10, 5))
plt.plot(epochs, train_losses, label='Train Loss')
plt.plot(epochs, val_losses, label='Validation Loss')

# 标注极小值
# plt.scatter(min_train_epoch, min_train_loss, color='blue')
# plt.text(min_train_epoch, min_train_loss * 0.5, f'Train Min\nEpoch: {min_train_epoch}\nLoss: {min_train_loss:.9f}', color='blue')
plt.scatter(min_val_epoch, min_val_loss, color='orange')
plt.text(min_val_epoch, min_val_loss * 1.5, f'Val Min\nEpoch: {min_val_epoch}\nLoss: {min_val_loss:.9f}', color='orange')

# 标注极大值
# plt.scatter(max_train_epoch, max_train_loss, color='green')
# plt.text(max_train_epoch, max_train_loss * 1.5, f'Train Max\nEpoch: {max_train_epoch}\nLoss: {max_train_loss:.9f}', color='green')
plt.scatter(max_val_epoch, max_val_loss, color='red')
plt.text(max_val_epoch, max_val_loss * 0.5, f'Val Max\nEpoch: {max_val_epoch}\nLoss: {max_val_loss:.9f}', color='red')

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Train and Validation Loss Over Epochs')
plt.legend()
plt.show()
