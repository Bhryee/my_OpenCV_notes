import cv2 as cv
import numpy as np

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/coins.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

gray = cv.GaussianBlur(gray, (9, 9), 2, 2)

circles = cv.HoughCircles(
    gray,
    cv.HOUGH_GRADIENT,
    dp=1,
    minDist=10,
    param1=100,
    param2=50,
    minRadius=20,
    maxRadius=100,
)

#dp = 1 resmin çözünürlüğü ile ilgilidir. Girdi resmi ile aynı çözünürlükte çıktı elde ederiz
#minDist = 10 saptanan nesnenin merkezi ile minimum uzaklığını ifade eder
#param1 : kenar saptamada odaklanma ile ilgilidir.
#param2 : daireleri saptama basamağında kullanılır. Kenar tespitindeki geçişlerdeki odağı ayarlamaya yarar.
#min - maxRadius : min ve max yarıçap ile ilgili bilgilerdir.


if circles is not None:
    circles = np.uint16(np.around(circles)) #np.around : ondalık sayıları en yakın tam sayıya yuvarlar.
    for c in circles[0, :]:
        print(c)
        cx, cy, r = c
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
        cv.circle(src, (cx, cy), r, (0, 0, 255), 2, 8, 0)

cv.imshow("hough line demo", src)
cv.waitKey(0)
cv.destroyAllWindows()