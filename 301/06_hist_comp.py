import cv2 as cv

src1 = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/waddles.png")
src2 = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")
src3 = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/mononoke.jpg")

# cvtColor

hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

# calcHist

hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])

# normalize

cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist

# HISTCMP_CORREL

similarity1to2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
similarity1to3 = cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
similarity2to3 = cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)

print(similarity1to2)
print(similarity1to3)
print(similarity2to3)