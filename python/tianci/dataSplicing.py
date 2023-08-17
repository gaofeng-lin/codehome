import h5py
import numpy as np

def generate(filepath):
    f = h5py.File(filepath, 'r')
    n_frame = len(f.keys())
    XYT = np.zeros((0,3))
    UX = np.zeros((0,1))
    UY = np.zeros((0,1))
    P = np.zeros((0,1))
    for key in f.keys():
        time = float(key)
        XY = f[key][:,0:2]
        ux = f[key][:,2][:,None]
        uy = f[key][:,3][:,None]
        p = f[key][:,4][:,None]
        XYT = np.concatenate((XYT, np.concatenate((XY, np.full((XY.shape[0],1), time)), axis=1)), axis=0)
        UX = np.concatenate((UX, ux), axis=0)
        UY = np.concatenate((UY, uy), axis=0)
        P = np.concatenate((P, p), axis=0)
    X, y = {}, {}
    X['data'] = XYT
    y['data'] = np.concatenate((UX, UY, P), axis=1)

    frame_data = np.hstack((XYT, y['data']))

    return frame_data

origin_frame_data = generate("C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\data_16_v2.h5")
new_frame_data = generate("C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\add_data.h5")




print(new_frame_data)

breakpoint()

merged_arr = np.vstack((origin_frame_data, new_frame_data))

# 按照t值（即索引为2的列）排序
sorted_indices = np.argsort(merged_arr[:, 2])
sorted_arr = merged_arr[sorted_indices]

# print(sorted_arr)



# # 使用字典分组
grouped = {}
for row in sorted_arr:
    t_value = row[2]
    if t_value not in grouped:
        grouped[t_value] = []
    grouped[t_value].append(row)

# # 迭代每个分组并打印相同 t 值的行
# for t_value, rows in grouped.items():
#     print(f"Rows with t={t_value}:")
#     for row in rows:
#         print(row)
#         # breakpoint()
#     print("------")


# 创建每个t值对应的numpy数组
arrays_for_t_values = {}

for t_value, rows in grouped.items():
    arrays_for_t_values[t_value] = np.vstack(rows)

# 打印每个t值的数组
count = 0
writeH5File = h5py.File('C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\data_extension.h5', 'w')
for t_value, arr in arrays_for_t_values.items():
    print(f"Array for t={t_value}:")
    # print(arr)
    print(arr.shape)
    writeH5File.create_dataset('{:0>5.1f}'.format(float(t_value)), data=arr)
    print("------")
    count = count + len(arr)

# t = np.linspace(0, 30, 101)
writeH5File.close()
# print('count is : ', count)

# writeH5File = h5py.File('C:\\Users\\76585\\Desktop\\天池结果文件v2\\dataExtension\\data_extension.h5', 'w')

# for time in t:
#     selected_rows = sorted_arr[np.isin(sorted_arr[:, 2], time)]
#     writeH5File.create_dataset('{:0>5.1f}'.format(float(time)), data=selected_rows)
# writeH5File.close()

