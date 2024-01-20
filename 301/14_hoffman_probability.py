#Hoffman Olasılıksal Çizgi Tespiti

import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(src, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/shapes.jpg")

binary = canny_demo(src)
cv.imshow("shapes_canny", binary)
cv.waitKey(2000)

linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 55, None, 50, 10)
cv.HoughLinesP
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(src, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv.LINE_AA)

cv.imshow("hough line demo", src)
cv.waitKey(2000)
