# pylint: disable=no-member

"""
openv demo
"""

import numpy as np
import cv2 as cv
import pytesseract


def zh_ch(string):
    return string.encode("gbk").decode(errors="ignore")


def display_image(image_path):
    """
    使用OpenCV显示图像。

    参数:
      image_path (str): 图像文件的路径。

    返回:
      None
    """
    img = cv.imread(image_path)

    cv.imshow(zh_ch("图片"), img)
    cv.waitKey(0)  # 等待窗口中的按键


def display_video(video_path):
    """
    使用OpenCV显示视频。

    参数:
      video_path (str): 视频文件的路径。

    返回:
      None
    """
    cap = cv.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow(zh_ch("视频"), gray)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


def display_camera():
    """
    使用OpenCV显示摄像头。

    参数:
      None

    返回:
      None
    """
    cap = cv.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow(zh_ch("摄像头"), gray)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


def draw_line():
    """
    使用OpenCV绘制线条。

    参数:
      None

    返回:
      None
    """
    img = np.zeros((512, 512, 3), np.uint8)

    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 255))

    cv.putText(
        img,
        zh_ch("OpenCV"),
        (10, 500),
        cv.FONT_HERSHEY_SIMPLEX,
        4,
        (255, 255, 255),
        2,
        cv.LINE_AA,
    )

    cv.imshow(zh_ch("绘制线条"), img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def get_image_text(imgpath):
    """
    使用OpenCV识别图片中的文字，并返回文字内容。

    参数:
      imgpath (str): 图片文件的路径。

    返回:
      (str): 图片中的文字内容。
    """

    # 读取图片
    img = cv.imread(imgpath)

    # 转换为灰度图像
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 二值化
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # 去除噪声
    kernel = np.ones((3, 3), np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

    # 找到前景区域
    sure_bg = cv.dilate(opening, kernel, iterations=3)

    # 找到未知区域
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)

    # 标记
    ret, markers = cv.connectedComponents(sure_fg)

    # 为所有的标记加1，保证背景是0而不是1
    markers = markers + 1

    # 现在让所有的未知区域为0
    markers[unknown == 255] = 0

    # 分水岭算法
    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]

    # 识别文字
    text = pytesseract.image_to_string(img, lang="chi_sim")

    return text


def get_image_face(imgpath):
    """
    使用OpenCV识别图片中的人脸，并返回人脸图片。

    参数:
      imgpath (str): 图片文件的路径。

    返回:
      (str): 人脸图片。
    """

    # 读取图片
    img = cv.imread(imgpath)

    # 转换为灰度图像
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 加载人脸识别模型
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 识别人脸
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 绘制人脸框
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow(zh_ch("图片"), img)
    cv.waitKey(0)  # 等待窗口中的按键

    return img


if __name__ == "__main__":
    # imgpath = "apps/opencv/cert.png"
    imgpath = "apps/opencv/1234.jpg"
    # display_image(img)
    text = get_image_face(imgpath)
    print(text)
