#bir görseldeki belirli köşeleri tespit eder.

import cv2 as cv
import numpy as np

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/Chess.jpg")

def harris(image):
    blockSize = 2 #köşe tespiti için düşünülen komşuluk boyutu
    apertureSize = 3 #sobel yöntemi için diyafram parametresi
    k = 0.04 #haresin serbestlik parametresi

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype=np.float32) # resimle aynı boyutta boş bir array oluşturulur.
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX) #array normalize edilir.

    #tespit edeceğimiz köşelerin etrafında dönerek köşeleri daire içine alır.
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i,j]) > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)
    return image

result = harris(src)
cv.imshow("result", result)
cv.waitKey(2000)

