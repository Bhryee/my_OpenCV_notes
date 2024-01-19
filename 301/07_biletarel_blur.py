import cv2 as cv
# filtreleme sırasında kullanılan  her bir piksel komşusunun çapı.
#sigma color= renk uzayındaki değeri verir. sayı ne kadar uzak olursa birbirine uzak renkler karışmaya başlar
# sigma space sayı ne kadar büyük olursa daha fazla piksel birbirine karıştırılıyor olucak

import cv2 as cv
import numpy as np

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(4000)

h, w = src.shape[:2]
dst = cv.bilateralFilter(src, 0, 100, 5)
"""filtreleme sırasında kullanılan her bir piksel komşusunun çapı

   sigma colour = renk uzayındaki değerdir. sayı ne kadar uzak olursa
   birbirine uzak renkler karışmaya başlar.
   sigma space = sayı ne kadar büyük olursa daha fazla piksel birbirine karıştırılır."""

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w : 2 * w, :] = dst

cv.imshow("result", result)
cv.waitKey(4000)
