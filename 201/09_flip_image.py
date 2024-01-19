import cv2 as cv

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img = cv.imread(path + "foto.jpg")


#X FLIP
dst1 = cv.flip(img, 0)
cv.imshow("foto x flip", dst1)
cv.waitKey(2000)


#Y FLIP
dst2 = cv.flip(img, 1)
cv.imshow("foto y flip", dst2)
cv.waitKey(1000)


#XY FLIP
dst3 = cv.flip(img, -1)
cv.imshow("foto xy flip", dst3)
cv.waitKey(10000)