# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from aukit import audio_noise_remover

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import openface


# 初始化OpenFace人脸检测器
align = openface.AlignDlib("shape_predictor_68_face_landmarks.dat")

# 加载要检测的图像
image_path = "1.jpg"  # 替换为你的图像路径
image = openface.load_image(image_path)

# 进行人脸检测
bounding_box = align.getLargestFaceBoundingBox(image)

if bounding_box is not None:
    # 在图像中绘制人脸边界框
    openface.draw_rect(image, bounding_box)

    # 保存带有边界框的图像
    output_path = "output_image.jpg"
    openface.save_image(image, output_path)

    print("人脸检测完成，结果已保存至", output_path)
else:
    print("未检测到人脸")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
