import cv2 as cv
import numpy as np
import os
os.system('python 图片获取.py')
img = cv.imread('temp-bf.jpg')
# 在图像上画矩形框
x1 = -1
y1 = -1
x2 = -1
y2 = -1

# canvas = np.zeros((300, 300, 3), dtype=np.uint8)
canvas = cv.imread('temp-bf.jpg', cv.IMREAD_COLOR)
img = np.copy(canvas)


# 回调，系统调用回调函数解决你的问题
# 鼠标响应回调函数，参数固定；对应鼠标事件、横坐标、纵坐标、flags和其他参数
def mouse_drawing(event, x, y, flags, param):
    # print(x, y)
    global x1, y1, x2, y2
    if event == cv.EVENT_LBUTTONDOWN:
        fileName = '翻译位置.txt'
        with open(fileName, 'w') as file:
            file.write(str(x)+"\n"+str(y)+"\n")
        x1 = x
        y1 = y
    if event == cv.EVENT_MOUSEMOVE:
        if x1 < 0 or y1 < 0:
            return
        x2 = x
        y2 = y
        dx = x2 - x1
        dy = y2 - y1
        if dx > 0 and dy > 0:
            # 擦除重叠
            # canvas[:, :] = 0
            canvas[:, :, :] = img[:, :, :]
            cv.rectangle(canvas, (x1, y1), (x2, y2), (255, 0, 0), 2, 8, 0)
    if event == cv.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        dx = x2 - x1
        dy = y2 - y1
        fileName = '翻译位置.txt'
        with open(fileName, 'a') as file:
            file.write(str(x)+"\n"+str(y))
        if dx > 0 and dy > 0:
            # canvas[:, :] = 0
            canvas[:, :, :] = img[:, :, :]
            cv.rectangle(canvas, (x1, y1), (x2, y2), (255, 0, 0), 2, 8, 0)

        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1


def mouse_response():
    cv.namedWindow('Mouse Response', cv.WINDOW_AUTOSIZE)
    # 再某个窗口上设置鼠标响应函数
    cv.setMouseCallback('Mouse Response', mouse_drawing)
    cv.moveWindow('Mouse Response',0,0)
    while True:
        cv.imshow('Mouse Response', canvas)
        c = cv.waitKey(1)
        if c == 27:
            break

    cv.destroyAllWindows()


if __name__ == '__main__':
    mouse_response()
