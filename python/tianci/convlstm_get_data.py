import numpy as np

# 假设data为你的原始数据，形状为(256*61, 3)
data = np.random.rand(256*61, 3)  # 这里仅为示例，你可以用自己的数据替换它

# 初始化
feature_sequence_length = 10
label_sequence_length = 20
time_slices = data.shape[0] // 256
features = []
labels = []

# 对每一个时间窗口进行滑动
for start in range(0, time_slices - feature_sequence_length - label_sequence_length + 1):
    end_feature = start + feature_sequence_length
    end_label = end_feature + label_sequence_length
    
    feature_slice = data[start*256:end_feature*256].reshape(feature_sequence_length, 3, 16, 16)
    label_slice = data[end_feature*256:end_label*256].reshape(label_sequence_length, 3, 16, 16)
    
    features.append(feature_slice)
    labels.append(label_slice)

# 转换为numpy数组
features = np.array(features)
labels = np.array(labels)

print(features.shape)  # 应该输出(32, 10, 3, 16, 16)
print(labels.shape)   # 应该输出(32, 20, 3, 16, 16)
