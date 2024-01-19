#Bir bilgisayarın fotoğraftaki kenarları anlaması demek renk geçişlerini anlaması demektir.
#sobel bir görüntüde x ve y eksenine göre  türevler hesaplayıp kenar algılamayı sağlar.

import cv2 as cv
import numpy as np
src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")

h, w = src.shape[:2]

#CV_32F : türev alma işlemidir
x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)  #x'e göre
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)  #y'ye göre

#türevleri ölçeklendirip mutlak değerini alma işlemidir.
x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

cv.imshow("x_grad", x_grad)
cv.waitKey(4000)

cv.imshow("y_grad", y_grad)
cv.waitKey(3000)

dst = cv.add( x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)

cv.imshow("gradient", dst)
cv.waitKey(3000)
