# coding=utf-8
from io import BytesIO

from PIL import Image


def get_gap(image1):
    left = 0
    for i in range(left, image1.size[0]):
        node = 0
        flag = 0
        for j in range(image1.size[1]):
            if is_pixel_equal(image1, i, j):
                left = i
                node += 1
                if not flag:
                    flag = j
                if abs(i - flag) > 45:
                    flag = 0
                if node > 40:
                    print "达标像素点"
                    print node
                    print "缺口位置", i + 18, j
                    return left + 18
                print(node)
            else:
                node = 0
                continue
    print("缺口识别失败", left)
    return 0


def is_pixel_equal(image1, x, y):
    """
    判断两个像素是否相同
    :param image1: 图片1
    :param image2: 图片2
    :param x: 位置x
    :param y: 位置y
    :return: 像素是否相同
    """
    # 取两个图片的像素点
    pixel1 = image1.load()[x, y]
    try:
        pixel2 = image1.load()[x + 1, y + 1]
    except:
        pixel2 = pixel1
    print pixel1[0], pixel1[1], pixel1[2]
    threshold = 0  # 三通道像素差值
    # if abs(pixel1[0] - pixel2[0]) > threshold and abs(pixel1[1] - pixel2[1]) > threshold and abs(
    #         pixel1[2] - pixel2[2]) > threshold:
    if pixel1[0] == 255 and pixel1[1] == 255 and pixel1[2] == 255:
        # print(pixel1, pixel2)
        # print("r:", pixel1[0] - pixel2[0])
        # print("g:", pixel1[1] - pixel2[1])
        # print("b:", pixel1[2] - pixel2[2])
        # if pixel1[0] > threshold and pixel1[1] > threshold and pixel1[2] > threshold:
        print "white"
        return True
    else:
        return False


if __name__ == '__main__':
    fp = open("./pic.png", mode="rb")
    image = Image.open(BytesIO(fp.read()))
    get_gap(image)
