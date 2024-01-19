import cv2 as cv

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"

img = cv.imread(path + "mononoke.jpg")
cv.namedWindow("renkli", cv.WINDOW_AUTOSIZE)
cv.imshow("renkli", img )
cv.waitKey(2000)


#cvtColor = renk değiştirir
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)# BGR to gray
""" R = red
    G = green
    B = blue """
cv.imshow("gri", gray)
cv.waitKey(2000)

#yaptığımız görseli kaydetmek için
cv.imwrite(path + "gray_mononoke.png", gray)
#yol + kaydetmek istediğimiz isim + kaydetmek istediğimiz görsel


#görseli en baştan gri okumak için:
img = cv.imread(path + "mononoke.jpg", cv.IMREAD_GRAYSCALE) #gri skalasında oku
cv.namedWindow("renkli", cv.WINDOW_AUTOSIZE)
cv.imshow("renkli", img )
cv.waitKey(2000)