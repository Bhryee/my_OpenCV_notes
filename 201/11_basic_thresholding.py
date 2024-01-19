

import cv2 as cv

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"

img = cv.imread(path + "foto.jpg")

T = 127 # gri rengi

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

"""girdi görüntüsüne göre optimum eşik değerini otomatik hesaplayarak
   bize farklı farklı formatlarda görsel elde etmemizi sağlicak."""
for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)
    cv.waitKey(1000)