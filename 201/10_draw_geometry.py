import cv2 as cv
import numpy as np

img = np.zeros([512,512,3], dtype = np.uint8)

# uint8 = (işaretsiz 8 bit tamsayı)

cv.rectangle(img, (100, 100), (300, 300), (255, 0, 0), 2, cv.LINE_8, 0)
cv.circle(img, (256, 256), 50, (0, 0, 255), 2, cv.LINE_8, 0)
cv.ellipse(img, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv.LINE_8, 0)

cv.imshow("image", img)
cv.waitKey(10000)


for i in range(100000):
    img[:, :, :] = 0
    x1 = np.random.rand() * 512
    y1 = np.random.rand() * 512
    x2 = np.random.rand() * 512
    y2 = np.random.rand() * 512

    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)

    cv.line(img, (np.int64(x1), np.int64(y1)), (np.int64(x2), np.int64(y2)), (b, g, r), 4, cv.LINE_8, 0)
    cv.rectangle(img, (np.int64(x1), np.int64(y1)), (np.int64(x2), np.int64(y2)), (b, g, r), 1, cv.LINE_8, 0)
    cv.imshow("image", img)

    c = cv.waitKey(30)
    if c == 27:
        break # ESC