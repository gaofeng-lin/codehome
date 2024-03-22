


import os
from PIL import Image

def remove_title_from_image(image_path, output_path, crop_height):
    with Image.open(image_path) as img:
        width, height = img.size
        # 假设标题在图像顶部，我们需要裁剪掉顶部的一部分
        # 这里的crop_height是需要裁剪的高度
        crop_rectangle = (0, crop_height, width, height)
        cropped_img = img.crop(crop_rectangle)
        cropped_img.save(output_path)

# 指定包含图像的文件夹路径和保存修改后图像的文件夹路径
input_folder = 'C:/Users/76585/OneDrive/metting_exp_etl/exp/202311中文期刊投稿/英文期刊/sn-article-template/picture/before_change'  # 替换为包含您图像的文件夹路径
output_folder = 'C:/Users/76585/OneDrive/metting_exp_etl/exp/202311中文期刊投稿/英文期刊/sn-article-template/picture/after_change'  # 替换为保存修改后图像的文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 您需要根据实际图像确定裁剪的高度
crop_height = 38  # 这个值需要根据您的图像标题的高度来调整

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        file_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        remove_title_from_image(file_path, output_path, crop_height)
