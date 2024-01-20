import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(src, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/sudoku.jpg")

binary = canny_demo(src)
cv.imshow("sudoku_canny", binary)
cv.waitKey(2000)

#sınır tanımlarındaki boşluklara torelanslıdır. Görüntüde yer alan gürültülerden etkilenmez.Görüntünün desenini takip eder.
lines = cv.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:
    for i in range (0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

cv.imshow("src", src)
cv.waitKey(2000)