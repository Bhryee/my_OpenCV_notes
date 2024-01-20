#otomatik görüntü eşikleme yöntemidir.
#giriş olarak verilen görüntüyü ikili görüntüye çevirir.
#pikselleri verilen eşik değerine göre siyah ya da beyaz olarak günceller.

import cv2 as cv
import numpy as np

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

h, w = src.shape[:2]

cv.imshow("image", binary)
cv.waitKey(2000)