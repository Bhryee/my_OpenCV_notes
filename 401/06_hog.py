#HOG (Histogram of Oriented Gradients)
import cv2 as cv
import numpy as np

src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/people_foto.jpg")

#HOGDecriptor : makine öğrenmesinde bir sınıflandırıcı yöntemdir.
hog = cv.HOGDescriptor()

#hog.setSVMDetector() fonksiyonu, hog adlı bir HOGDescriptor nesnesinin SVM dedektörünü ayarlar.
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.25)

"""winStride : Pencerenin kaydırma adımlarını belirler.
               Pencerenin kaydırma adımları ne kadar büyük olursa,
               pencere o kadar hızlı hareket eder ve daha fazla nesne tespit edilir.
               
   padding : Pencerenin kenarlarındaki boşlukları belirler.
             Boşluklar ne kadar büyük olursa, pencere o kadar büyük olur
             ve daha küçük nesneler tespit edilebilir.
             
   scale : Pencerenin ölçek faktörünü belirler.
           Ölçek faktörü ne kadar büyük olursa, pencere o kadar büyük olur
           ve daha küçük nesneler tespit edilebilir."""

for x, y, w, h in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv.imshow("hog", src)
cv.waitKey(2000)