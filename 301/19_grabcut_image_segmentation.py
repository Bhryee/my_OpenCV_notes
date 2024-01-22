import cv2 as cv
import numpy as np

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/coins.jpg")
src = cv.resize(src, (0, 0), fx=0.5, fy=0.5)

r = cv.selectROI("input", src, False)
cv.destroyAllWindows()  # "input" penceresini kapat

roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
img = src.copy()

cv.rectangle(
    img,
    (int(r[0]), int(r[1])),
    (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])),
    (255, 0, 0),
    2,
)

mask = np.zeros(src.shape[:2], dtype=np.uint8)
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8") * 255
result = cv.bitwise_and(src, src, mask=mask2)

cv.imshow("result", result)
cv.waitKey(0)
cv.destroyAllWindows()
