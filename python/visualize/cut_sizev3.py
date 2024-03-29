import os
from PIL import Image

def crop_image_to_remove_border(image_path, output_path):
    # 打开图片
    with Image.open(image_path) as image:
        # 获取图片的尺寸和像素数据
        pixdata = image.load()
        width, height = image.size

        # 定义查找边框的函数
        def find_border_color():
            colors = {}
            # 检查四个边缘以确定最常见的颜色
            for x in range(width):
                for y in [0, height - 1]:
                    color = pixdata[x, y]
                    colors[color] = colors.get(color, 0) + 1
            for y in range(height):
                for x in [0, width - 1]:
                    color = pixdata[x, y]
                    colors[color] = colors.get(color, 0) + 1
            # 返回最常见的颜色
            return max(colors, key=colors.get)

        border_color = find_border_color()

        # 找到非边框颜色的最小包围矩形
        left = width
        right = 0
        top = height
        bottom = 0

        for y in range(height):
            for x in range(width):
                if pixdata[x, y] != border_color:
                    if x < left:
                        left = x
                    if x > right:
                        right = x
                    if y < top:
                        top = y
                    if y > bottom:
                        bottom = y

        # 根据找到的边界裁剪图片
        cropped_image = image.crop((left, top, right, bottom))

        # 保存裁剪后的图片
        cropped_image.save(output_path)

def crop_all_tiff_images_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.tiff') or file_name.endswith('.tif'):
            image_path = os.path.join(folder_path, file_name)
            output_path = os.path.join(folder_path, 'convert',file_name.replace('.tif', '_cropped.tif').replace('.tiff', '_cropped.tiff'))
            crop_image_to_remove_border(image_path, output_path)
            print(f"Cropped and saved: {output_path}")

def single_image(folder_path):
    file_name = "v1.tiff"
    image_path = os.path.join(folder_path, file_name)
    output_path = os.path.join(folder_path, 'convert',file_name.replace('.tif', '_cropped.tif').replace('.tiff', '_cropped.tiff'))
    crop_image_to_remove_border(image_path, output_path)
    print(f"Cropped and saved: {output_path}")

# 将folder_path变量更改为你的文件夹路径
folder_path = 'C:/Users/76585/Desktop/test/weno3d-inter'
crop_all_tiff_images_in_folder(folder_path)
# single_image(folder_path)
