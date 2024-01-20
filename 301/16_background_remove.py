import cv2 as cv

cap = cv.VideoCapture("/Users/bahriyeisgor/Desktop/OpenCV/videos/video.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=20)
#history : Gecikmelere (video akarkenki her pencere) ne kadar odaklanacağımızı ifade eder.
#varThreshoold : Varyans Threshold. Videoda odaklanacak olduğumuz görüntüye ne kadar hassas olduğumuzu ifade eder.

while True:
    # Video çerçevesini oku
    ret, frame = cap.read()

    # Eğer çerçeve başarıyla okunamazsa döngüden çık
    if not ret:
        break

    # Foreground maskesini ve background görüntüsünü al
    fgmask = fgbg.apply(frame) #siyah arka plana ait yapıyı buradan elde ediyoruz.
    background = fgbg.getBackgroundImage() #

    # Görüntüleri göster
    cv.imshow("input", frame)
    cv.imshow("mask", fgmask)
    cv.imshow("background", background)

    # 'ESC' tuşu ile döngüden çık
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break

cap.release()