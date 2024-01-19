"""bir resimdeki her bir pikselin mevcut x ve y konumundan
   yeni bir x y konumuna dönüştürülmesidir.
   yani kaydırma işlemi."""

import cv2 as cv
import numpy as np

#shifting = kaydırma

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img = cv.imread(path + "foto.jpg")

rows = img.shape[0] #resmin x koordinatını alır
cols = img.shape[1] # y koordinat

M= np.float32([[1,0,300], [0,1,90]])

shifted = cv.warpAffine(img, M, (cols, rows)) # resmin bilgisi, çıktısı, satır sütun

cv.imshow("original", img)
cv.waitKey(1000)

cv.imshow("Shift", shifted)
cv.waitKey(1000) #sağ ve aşşağı kaydırıldı


#rotation = döndürme
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("rotation", dst)
cv.waitKey(1000)


#scaling

#fx ve fy'de büyütmek için 1'den büyük, küçültmek için 1'den küçük sayılar girilmeli 
res = cv.resize(img, None, fx=0.25, fy=0.25, interpolation = cv.INTER_CUBIC)

cv.imshow("scaling", res)
cv.waitKey(1000)




