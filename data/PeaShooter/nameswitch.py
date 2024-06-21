import os


def rename_images():
    # 获取当前文件夹下所有文件
    files = os.listdir('.')

    # 统计图片文件数量
    image_count = 0
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_count += 1

    # 对图片文件进行重新命名
    index = 1
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # 构建新的文件名
            file_name, file_ext = os.path.splitext(file)
            new_name = f"peashooter{index}{file_ext}"

            # 重命名文件
            os.rename(file, new_name)
            print(f"Renamed {file} to {new_name}")

            index += 1

    print(f"Renamed {image_count} image files.")


# 调用函数来执行重命名操作
rename_images()
