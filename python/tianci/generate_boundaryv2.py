import numpy as np

# 这个代码的作用是找到边界上的点，要优先满足目标文件上的边界点，然后在此基础上进行扩充

def generateBoundary(new_points):

    # 定义范围和间隔
    x_values = np.linspace(-np.pi, np.pi - 2*np.pi/512, 512)
    y_values = np.linspace(-np.pi, np.pi - 2*np.pi/512, 512)

    # 创建一个二维的点集
    X, Y = np.meshgrid(x_values, y_values)

    # 找到x=-pi的点
    x_left_boundary = X[X == -np.pi]
    y_left_boundary = Y[X == -np.pi]

    # 找到y=-pi的点
    x_bottom_boundary = X[Y == -np.pi]
    y_bottom_boundary = Y[Y == -np.pi]

    # 为x=-pi的点生成对应的点
    x_corresponding_to_left = np.pi * np.ones_like(x_left_boundary)
    y_corresponding_to_left = y_left_boundary

    # 为y=-pi的点生成对应的点
    x_corresponding_to_bottom = x_bottom_boundary
    y_corresponding_to_bottom = np.pi * np.ones_like(y_bottom_boundary)




    # 确定新点的数量
    new_points = 2000  # 举例

    # 使用linspace在-pi和pi范围内均匀生成new_points个点
    new_boundary_values = np.linspace(-np.pi, np.pi, new_points)

    # 创建新的边界点
    x_new_left = -np.pi * np.ones_like(new_boundary_values)
    y_new_left = new_boundary_values



    x_new_right = np.pi * np.ones_like(new_boundary_values)
    y_new_right = new_boundary_values



    x_new_bottom = new_boundary_values
    y_new_bottom = -np.pi * np.ones_like(new_boundary_values)

    x_new_top = new_boundary_values
    y_new_top = np.pi * np.ones_like(new_boundary_values)

    # 如果你想将这些点与原始点合并，你可以使用 np.concatenate
    x_left_total = np.concatenate((x_left_boundary, x_new_left))
    y_left_total = np.concatenate((y_left_boundary, y_new_left))

    left_total = np.column_stack((x_left_total, y_left_total))

    # print("Points on the left boundary:")
    # print(left_total)

    x_right_total = np.concatenate((x_corresponding_to_left, x_new_right))
    y_right_total = np.concatenate((y_corresponding_to_left, y_new_right))

    right_total = np.column_stack((x_right_total, y_right_total))

    # print("\nCorresponding points for the left boundary:")
    # print(right_total)

    x_bottom_total = np.concatenate((x_bottom_boundary, x_new_bottom))
    y_bottom_total = np.concatenate((y_bottom_boundary, y_new_bottom))

    bottom_total = np.column_stack((x_bottom_total, y_bottom_total))

    x_top_total = np.concatenate((x_corresponding_to_bottom, x_new_top))
    y_top_total = np.concatenate((y_corresponding_to_bottom, y_new_top))

    top_total = np.column_stack((x_top_total, y_top_total))




    left_boundary = addTimeToBoundary(new_points + 512, left_total)
    right_boundary = addTimeToBoundary(new_points + 512, right_total)
    bottom_boundary = addTimeToBoundary(new_points + 512, bottom_total)
    top_boundary = addTimeToBoundary(new_points + 512, top_total)

    total_boundary = np.vstack((left_boundary, right_boundary, bottom_boundary, top_boundary))

    return total_boundary

def addTimeToBoundary(each_slice_point_num, XYCoordinate):
    result = []
    t = np.linspace(0, 30, 101)
    for time_value in t:
        # 创建一个全为 time_value 的列向量
        time_column = np.full((each_slice_point_num, 1), time_value)

        # 拼接时间列和 data_array
        new_data = np.hstack((XYCoordinate, time_column))

        result.append(new_data)
    res = np.vstack((result))

    return res

# 现在，result 是一个列表，其中包含 101 个 (101, 3) 的数组。

new_points = 2000
boundary_inputs = generateBoundary(new_points)
print('boundary_inputs is: ', boundary_inputs.shape)

split_num = (new_points + 512) * 101

left = boundary_inputs[:split_num]
right = boundary_inputs[split_num:2*split_num]
bottom = boundary_inputs[2*split_num:3*split_num]
top = boundary_inputs[3*split_num:]

print('bottom  is: ',bottom)

print('top  is: ',top)