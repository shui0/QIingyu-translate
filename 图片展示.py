import cv2 as cv
import os
while True:
    # #图片获取
    os.system("python 图片获取.py")
    # #图片翻译
    os.system("python 识别+翻译.py")
    location = open("翻译位置.txt", 'r')
    x1 = location.readline()
    y1 = location.readline()
    x2 = location.readline()
    y2 = location.readline()
    img = cv.imread("temp-af.jpg")
    img = img [int(x1):int(x2),int(y1):int(y2)]
    cv.imshow('res_show', img)
    cv.resizeWindow('res_show',int(x2)-int(x1),int(y2)-int(y1))
    if ord('q') == cv.waitKey(0):
        break
cv.destroyAllWindows()