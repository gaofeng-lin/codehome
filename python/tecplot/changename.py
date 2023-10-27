import os

# 指定包含原始文件的文件夹路径
folder_path = 'C:/Users/76585/Desktop/origin_dat_change_name/'

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 遍历文件并更改文件名
count = 1
for file_name in files:
    # 检查文件名是否以 "tecplot_data_" 开头且以 ".dat" 结尾
    if file_name.startswith("tecplot_data_") and file_name.endswith(".dat"):
        # 构建新的文件名
        new_file_name = f"{count:03d}.dat"
        
        # 构建完整的文件路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        
        # 增加计数器
        count += 1

print("文件名更改完成。")
