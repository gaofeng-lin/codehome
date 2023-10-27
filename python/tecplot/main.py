import os

# 定义文件夹路径
directory = "C:\\Users\\76585\\Desktop\\tecplot\\238\\"

# 获取所有的 .dat 文件
dat_files = [f for f in os.listdir(directory) if f.endswith('.dat')]

# 打开宏文件进行写入
with open(os.path.join(directory, 'load_and_save.mcr'), 'w') as mcr:
    for dat_file in dat_files:
        # 完整的文件路径
        full_path = os.path.join(directory, dat_file)
        
        # 输出文件名
        output_name = os.path.splitext(dat_file)[0] + ".png"
        output_path = os.path.join(directory, output_name)
        
        mcr.write(f"$!ReadDataSet  \"{full_path}\"\n")
        mcr.write("ReadDataOption = Replace\n")
        mcr.write(f"$!Export \n")
        mcr.write("SetupFile = \"\"\n")
        mcr.write(f"ExportFName = \"{output_path}\"\n")
        mcr.write("ImageWidth = 1280\n")
        mcr.write("ImageHeight = 720\n")
        mcr.write("SuperSampleFactor = 1\n")
        mcr.write("ImageFormat = PNG\n")
        mcr.write("UseScreenResolution = No\n")
        mcr.write("MaintainAspectRatio = Yes\n\n")

print("宏文件已生成！")
