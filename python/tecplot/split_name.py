import os
import re

# 定义目标文件夹路径
folder_path = "C:/Users/76585/Desktop/origin_p_dat"
output_file = "C:/Users/76585/Desktop/origin_p_dat/output.txt"

# 获取文件夹中的所有文件名
all_files = os.listdir(folder_path)

# 筛选出以"tecplot_data"开头的文件
tecplot_files = [f for f in all_files if f.startswith("tecplot_data")]

# 提取文件名中的数字并用于排序
def extract_number_from_filename(filename):
    match = re.search(r"(\d+\.\d+)", filename)
    if match:
        return float(match.group(1))
    return 0

tecplot_files = sorted(tecplot_files, key=extract_number_from_filename)

# 打开一个文件用于输出结果
with open(output_file, "w") as out:
    for file_name in tecplot_files:
        # 构造语句
        statement = f'<Element FilePath="{folder_path}/{file_name}"/>\n'
        
        # 写入文件
        out.write(statement)

print(f"语句已输出到{output_file}中.")
