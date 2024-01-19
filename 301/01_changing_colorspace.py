#RGB = renk uzayı
#HSV
""" Hue (Ton):
    Renk skalasını temsil eder.
    0 ila 360 arasında bir değer alır.
    Temel renkleri ifade eder, örneğin kırmızı, mavi, yeşil gibi.

    Saturation (Doygunluk):
    Renklerin canlılığını ve solgunluğunu temsil eder.
    0 ile 1 arasında bir değer alır.
    Doygunluk ne kadar yüksekse, renkler o kadar canlı olur.

    Value (Değer):
    Renklerin parlaklığını temsil eder.
    0 ile 1 arasında bir değer alır.
    Değer ne kadar yüksekse, renkler o kadar parlak olur."""


import cv2 as cv

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img = cv.imread( path + "foto.jpg")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(1000)

#rgb'den gray'e çevrim
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1000)

#hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(3000)