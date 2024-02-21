from PIL import Image

def crop_image_to_colored_region(image_path, output_path):
    # 打开图片
    image = Image.open(image_path)
    # 转换为RGBA，以便处理带有透明背景的图片
    image = image.convert("RGBA")
    
    # 获取图片的尺寸和像素数据
    pixdata = image.load()
    width, height = image.size
    
    # 初始裁剪边界
    left = width
    right = 0
    top = height
    bottom = 0
    
    # 遍历每个像素，找到非白色像素的最小包围矩形
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixdata[x, y]
            if a > 0 and (r < 255 or g < 255 or b < 255):  # 考虑透明度和非白色像素
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

# 使用示例
input_path = 'C:/Users/76585/OneDrive/metting_exp_etl/exp/202311中文期刊投稿/图片/可视化图/dm外推/convlstm32-t10.tiff'  # 更改为你的图片路径
output_path = 'C:/Users/76585/OneDrive/metting_exp_etl/exp/202311中文期刊投稿/图片/可视化图/dm外推/convlstm32-t10-cropped.tiff'  # 更改为你希望保存的路径和文件名

crop_image_to_colored_region(input_path, output_path)
