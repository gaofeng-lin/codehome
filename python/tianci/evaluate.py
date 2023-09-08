import numpy as np
from scipy.optimize import minimize

# 假设你有N组预测值和相对二范数误差
# 以列表的形式表示
predictions = [np.array([1.5, 2.5, 3.5]), 
               np.array([1.7, 2.8, 3.4]), 
               np.array([1.4, 2.3, 3.6])]
errors = [0.2, 0.15, 0.25]

# 定义损失函数
def loss_function(X, predictions, errors):
    squared_errors = np.array([np.linalg.norm(pred - X, ord=2) - err for pred, err in zip(predictions, errors)])
    return np.sum(squared_errors ** 2)

# 初始估计值
initial_guess = np.zeros_like(predictions[0])
# initial_guess = np.array([1.5, 2.5, 3.5])

# 使用最小二乘法进行优化
result = minimize(loss_function, initial_guess, args=(predictions, errors), method='Nelder-Mead')

# 输出估计的真实值
estimated_real_value = result.x
print("估计的真实值:", estimated_real_value)
