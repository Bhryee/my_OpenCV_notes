#contours : bir görüntüde bulunan nesnelerin şekillerini temsil eder.
#Görüntünün sahip olduğu tüm noktaları birleştiren kapalı bir eğri oluşturularak kontur oluşturulması.
import cv2 as cv
import numpy as np
src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")

def threshold_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow("binary", binary)
    return binary

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(src, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(3000)

binary = threshold_demo(src)

canny = canny_demo(src)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

cv.imshow("contours_demo", src)
cv.waitKey(5000)