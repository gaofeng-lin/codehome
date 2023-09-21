import numpy as np

def custom_loss(pred, target):
    # 预测值和真值每一项相减，平方
    squared_diff = (pred - target) ** 2

    # 真值每一项平方
    squared_target = target ** 2

    # 对每一列进行累加
    numerator = np.sum(squared_diff)
    denominator = np.sum(squared_target)

    # 两项相除
    ratio = numerator / (denominator)

    # 对每个比率开根号，并计算平均损失
    result = np.sqrt(ratio)
    
    return result

p_ux = np.array([1, 2, 3])
r_ux = np.array([3, 4, 5])

# res = np.sqrt((p_ux - r_ux) **2 / r_ux**2)
res = custom_loss(p_ux, r_ux)

print('res is : ', res)

