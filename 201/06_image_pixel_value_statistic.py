import cv2 as cv
import numpy as np

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img = cv.imread(path + "foto.jpg", cv.IMREAD_GRAYSCALE)

# minMaxLoc
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(img)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("minLoc:", min_loc, ",", "maxLoc:", max_loc)

# meanStdDev
means, stddev = cv.meanStdDev(img)
print("mean: %.2f, stddev: %.2f" % (means, stddev))

img[np.where(img < means)] = 0
img[np.where(img > means)] = 255

cv.imshow("binary", img)
cv.waitKey(10000)