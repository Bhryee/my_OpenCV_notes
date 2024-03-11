import cv2 as cv
import numpy as np

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
src = cv.imread(path + "qrcode.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

qrcoder = cv.QRCodeDetector()

codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)

codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)

print(points)

result = np.copy(src)

cv.drawContours(result, [np.int32(points)], 0,(0, 0, 255), 2)

print(codeinfo)

cv.imshow("hog", src)
cv.waitKey(2000)



