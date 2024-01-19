import cv2 as cv
import numpy as np

capture = cv.VideoCapture("/Users/bahriyeisgor/Desktop/OpenCV/videos/video.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT) #videonun yüksekliği
width = capture.get(cv.CAP_PROP_FRAME_WIDTH) #genişliği
count = capture.get (cv.CAP_PROP_FRAME_COUNT) #toplam kare sayısı 
fps = capture.get(cv.CAP_PROP_FPS) #saniyedeki kare sayısı
print(height, width, count, fps)

out = cv.VideoWriter("/Users/bahriyeisgor/Desktop/OpenCV/videos/video_save.mp4",
                     cv.VideoWriter.fourcc('D', 'I', 'V', 'X'), 60,
                     (np.int64(width), np.int64(height)), True)


"""
    codec = video sıkıştırma işlemi
    cv.VideoWriter.fourcc('D', 'I', 'V', 'X'): Bu kısım, kullanılan video codec'ini belirtir.
    Burada 'DIVX' codec'i kullanılıyor.
    fourcc, Four Character Code'nin kısaltmasıdır ve bir video codec'i temsil eder.

    60 değeri fps değeridir.

    (np.int64(width), np.int64(height)): Bu kısım, çıkış videonun genişliğini ve yüksekliğini belirtir.
    width ve height, önceki kısımda video nesnesinden alınan video özellikleridir.
    np.int64 kullanılarak genişlik ve yükseklik değerleri tamsayıya dönüştürülüyor.

   True: Bu kısım, renkli görüntü kullanılıp kullanılmayacağını belirtir.
   True ise renkli,
   False ise siyah-beyaz görüntü demektir."""


while True:
    # kameradan görüntü al
    ret, frame = capture.read()

     # görüntü başarıyla alındı mı kontrol et
    if ret is True:

         # okunan görüntüyü ekranda göster
        cv.imshow("video-input", frame)
        out.write(frame)

         # 10 saniye sonra çık
        c= cv.waitKey(10000)
        if c == 27: # ESC tuşuna basılırsa döngü kırılır
            break
    else:
        break

capture.release()
#out.release()