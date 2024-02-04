import numpy as np
import modred as mr

def prepare_data_for_POD(data, num_time_steps_to_predict):
    """
    将五维数据重构为适用于 POD 的格式。
    :param data: 原始五维数据 (batch_size, 时间步, 通道数, 高, 宽)
    :param num_time_steps_to_predict: 要预测的时间步数量
    :return: 重构后的数据
    """
    # 确保输入数据的形状为 (batch_size, 时间步, 通道数, 高, 宽)
    assert len(data.shape) == 5
    
    # 获取输入数据的维度
    batch_size, num_time_steps, num_channels, height, width = data.shape
    
    # 检查是否有足够的时间步来预测
    assert num_time_steps_to_predict <= num_time_steps

    # 将数据重构为二维数组，其中一维是空间信息，另一维是时间信息
    # 对于 POD，我们通常使用所有批次、通道和空间点的所有时间步
    reshaped_data = data.transpose(1, 0, 2, 3, 4).reshape(num_time_steps, -1)

    return reshaped_data

b=20
t=20
c=1
h=32
w=32
data = np.random.random((b, t, c, h, w))


# 假设 'data' 是你的五维输入数据
# 使用前 10 个时间步来预测后 10 个时间步
num_time_steps_to_predict = 10
vecs = prepare_data_for_POD(data, num_time_steps_to_predict)

# 计算 POD
num_modes = 5
POD_res = mr.compute_POD_arrays_snaps_method(
    vecs[:10], list(range(num_modes)))  # 使用前 10 个时间步
modes = POD_res.modes
eigvals = POD_res.eigvals

# 这里的 'modes' 和 'eigvals' 可以用来预测或重构数据
