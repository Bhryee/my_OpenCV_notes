#görüntüdeki nesne tespiti için kullanılır.

import cv2 as cv
import numpy as np
src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")

edge = cv.Canny(src, 100, 200)
cv.imshow("Canny_method", edge)
cv.waitKey(2000)