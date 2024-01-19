import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#görseller sayılardan oluşur ve görsellerdeki sayıların görselleştirilmesidir.

def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype = np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype = np.int32)
    plt.bar(y_pos, hist, align = 'center', color = 'r', alpha = 0.5)
    plt.xticks = (y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()



def image_hist(image):
    cv.imshow('input', image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        #fotoğraf, renklerin indexleri,histogramda kullanmak istediğimiz bir görsel varsa,ayrım noktaları ,histogramın boyutu
        hist = cv.calcHist([image], [i], None, [256], [0,256])
        plt.plot(hist, color = color)
        plt.xlim([0,256])
    plt.show()



src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("image", src)
cv.waitKey(1000)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
custom_hist(gray)

image_hist(src)