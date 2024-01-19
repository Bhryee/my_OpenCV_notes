#normalizastion = standartlaştırma
import cv2 as cv
import numpy as np

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"

img = cv.imread(path + "foto.jpg")
print(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
#cv.waitKey(1000)

print(gray.shape)

print(gray)

gray = np.float32(gray)
print(gray)

# minMaxLoc
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("minLoc:", min_loc, ",", "maxLoc:", max_loc)

# meanStdDev
means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

#0'lardan oluşan bir çıktı array oluşturalım.
dst = np.zeros(gray.shape, dtype = np.float32)

cv.normalize(gray, dst = dst, alpha= 0, beta=1.0, norm_type =cv.NORM_MINMAX)
#dst = çıktı array'i
#norm_type = normalizasyon tipi
#alpha ve beta = 0 ile 1 arasında bir dönüştürme yapmak istediğimizi söylüyoruz.
print(dst)

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1000)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))

means, stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

cv.imshow("NORM_MINMAX * 255", np.uint8(dst*255))
cv.waitKey(1000)