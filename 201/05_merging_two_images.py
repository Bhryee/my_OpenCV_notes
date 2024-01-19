import cv2 as cv
import numpy as np

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img1 = cv.imread(path + "mononoke1.jpg")
img2 = cv.imread(path + "mononoke2.jpg")

cv.imshow("mononoke_1", img1)
cv.waitKey(1000)

cv.imshow("mononoke_2", img2)
cv.waitKey(1000)

horizontal = np.hstack((img1, img2))
cv.imshow("mononoke", horizontal)
cv.waitKey(10000)