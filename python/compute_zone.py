def check_data_groups(filepath):
    with open(filepath, 'r') as file:
        line_number = 0  # 初始化行号
        for line in file:
            line_number += 1
            # 每3行为一组，检查第三行
            if line_number % 3 == 0:
                # 检查第三行是否只包含单个数据值
                data_values = line.strip().split()
                if len(data_values) != 1:
                    print(f"检测失败：第 {line_number} 行不只包含一个数据值。")
                    return  # 停止执行
    print("所有检测通过，每组的第三行都只有一个数据值。")

# 替换下面的路径为你的plt文件路径
filepath = 'C:/Users/76585/Desktop/RESU0059.plt'
check_data_groups(filepath)



# # 替换下面的路径为你的plt文件路径
# filepath = 'C:/Users/76585/Desktop/RESU0059.plt'
# zones_data = parse_plt_file(filepath)

# print("每个ZONE的数据点数目:", zones_data)
# print("总ZONE数量:", len(zones_data))
