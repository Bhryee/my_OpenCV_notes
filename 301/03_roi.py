#Region Of Interestt = ilgilenilen alan
#resim üzerinde bölgesel çalışma yapılmak istendiğinde kullanılır.
#örneğin yüzde sadece gözle çalışmak
import cv2 as cv

original = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")
h,w = original.shape[:2]
img = original.copy()

roi = img[300:750, 950:1500, :]
print(roi.shape[:2])

cv.imshow("roi", roi)
cv.waitKey(1000)


img[0:450, 0:490, :] = roi #resmin bu bölgesine roi'yi ata
cv.imshow("img", img)
cv.waitKey(1000)


res = cv.resize(roi, None, fx = 0.2, fy = 0.2, interpolation = cv.INTER_CUBIC)
cv.imshow("res", res)
cv.waitKey(1000)
res.shape[:2]


original[0:90, 0:98, :] = res
cv.imshow("img", original)
cv.waitKey(10000)


