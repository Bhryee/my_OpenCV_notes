#Hareketli Nesnelerden Arka Plan Çıkarma
#Hareket eden nesneleri takip edip arka plandan ayırma işlemi

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("/Users/bahriyeisgor/Desktop/OpenCV/videos/video.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=10)

def process(image):
    mask = fgbg.apply(image)
    line = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)
    cv.imshow("mask", mask)
    contours, hierarchy = cv.findContours(
        mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    for c in range(len(contours)):
        area = cv.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv.minAreaRect(contours[c])
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv.circle(
            image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0
        )
    return image


while True:
    ret, frame = cap.read()
    cv.imshow("input", frame)
    result = process(frame)
    cv.imshow("result", result)
    k = cv.waitKey(50) & 0xFF
    if k == 27:
        break
