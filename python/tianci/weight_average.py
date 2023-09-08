import numpy as np

# 假设的数据
predictions = [np.array([1.5, 2.5, 3.5]), 
               np.array([1.7, 2.8, 3.4]), 
               np.array([1.4, 2.3, 3.6])]
print(predictions[0].shape)

norms = np.array([0.2, 0.15, 0.25])  # 与真实数据的相对二范数

# 根据二范数计算权重 (越小的二范数意味着越大的权重)
weights = 1 / norms
normalized_weights = weights / np.sum(weights)

# 使用权重计算加权平均值
weighted_average = sum(pred * w for pred, w in zip(predictions, normalized_weights))

# 输出结果
print("加权平均预测:", weighted_average)

# 可视化
import matplotlib.pyplot as plt

for i, pred in enumerate(predictions):
    plt.plot(pred, label=f"Prediction {i+1}")

plt.plot(weighted_average, linestyle='--', color='black', label="Weighted Avg")
plt.legend()
plt.show()
