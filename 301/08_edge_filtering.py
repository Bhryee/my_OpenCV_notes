#Kenarları koruyarak filtreleme işlemleridir.
#edgePreservingFilter

import cv2 as cv
import numpy as np
src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")
cv.imshow("image", src)
cv.waitKey(1000)

#resmin boyut bilgileri
h, w = src.shape[:2]

dst = cv.edgePreservingFilter(src, sigma_s=100, sigma_r=0.1, flags=cv.RECURS_FILTER)
#sigma_s 0 ile 200 arasında değer alır. Bulurlama şiddetidir.
#sigma_r 0 ile 1 arasında değer alır. Kenar bölgelerin dikkate alınıp alınmayacağını ifade eder.

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst

result = cv.resize(result, (w, h // 2))
cv.imshow("result", result)
cv.waitKey(3000)
