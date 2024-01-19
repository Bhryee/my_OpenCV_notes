import numpy as np
import cv2 as cv
""" Resimler numpy formatında tutulur.
    Dolayısıyla sayılardan oluşan bir array'dir. """

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img = cv.imread(path + "mononoke.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", img)
cv.waitKey(1000)

m1 = np.copy(img) #m1'de yaptığım değişiklik img'i etkilemez.

m2 = img #m2'de yaptığım değişiklik img'i etkiler

#resmin belirli bir yerine gitmek için 3 kanal vardır:
img[100: 200, 200:300, :] = 255 # 255 = beyaz,    0 = siyah
cv.imshow("m2",m2)
cv.waitKey(1000)

#resimle aynı boyutta sıfırlar oluşturalım:
m3 = np.zeros(img.shape, img.dtype) #resmin boyunda ve tipinde 0'lar oluşturuyoruz.
cv.imshow("m3", m3)
cv.waitKey(2000)

#farklı boyutta sıfırlardan oluşan farklı bir görsel oluşturma:
m4 = np.zeros([512, 512], np.uint8)
cv.imshow("m4", m4)
cv.waitKey(1000)

#gri görsel oluşturma
m5 = np.zeros([512, 512], np.uint8)
m5[:,:] = 127
cv.imshow("m5", m5)
cv.waitKey(1000)


#her bir hücre bir rengi temsil ediyor
img = np.ones((550,770,3))
black = (0,0,0)
red = (0,0,255)
green = (0,255,0) #RGreenB


#rectangle = dikdörtgen
cv.rectangle(img, (480,250), (100,450), black, 8)
cv.rectangle(img, (580,150), (200,350), black, 8)
cv.line(img, (100,450), (200,350), black, 8)
cv.line(img, (480,250), (580,150), black, 8)
cv.line(img, (100,250), (200,150), black, 8)
cv.line(img, (480,450), (580,350), black, 8)

start_point = (150,100)
font_thickness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX

cv.putText(img, "kutu", start_point, font, font_size, black ,font_thickness )
cv.imshow("dikdörtgen", img)
cv.waitKey(1000)
