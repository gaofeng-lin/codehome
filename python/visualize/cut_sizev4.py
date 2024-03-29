from PIL import Image, ImageOps

# 这个代码是切割数值条

def crop_inner_black_box(image_path, output_path):
    # 打开图片
    img = Image.open(image_path)

    # 获取图片的尺寸
    width, height = img.size

    # 定义黑色像素颜色
    black_color = (0, 0, 0)  # 假设黑色为 RGB (0, 0, 0)

    # 寻找左边缘
    left_edge = None
    for x in range(width):
        if img.getpixel((x, height // 2)) == black_color:
            left_edge = x
            break

    # 寻找右边缘
    right_edge = None
    for x in range(width - 1, -1, -1):
        if img.getpixel((x, height // 2)) == black_color:
            right_edge = x
            break

    # 寻找上边缘
    top_edge = None
    for y in range(height):
        if img.getpixel((width // 2, y)) == black_color:
            top_edge = y
            break

    # 寻找下边缘
    bottom_edge = None
    for y in range(height - 1, -1, -1):
        if img.getpixel((width // 2, y)) == black_color:
            bottom_edge = y
            break

    # 截取黑色框及框内内容
    cropped_img = img.crop((left_edge + 1, top_edge + 1, right_edge, bottom_edge))

    # 保存截取后的图片
    cropped_img.save(output_path)
# 调用函数进行截取
input_image_path = 'C:/Users/76585/Desktop/ffs-range.png'  # 输入图片路径
output_image_path = 'C:/Users/76585/Desktop/ffs-rangev2.png'  # 输出图片路径
crop_inner_black_box(input_image_path, output_image_path)
