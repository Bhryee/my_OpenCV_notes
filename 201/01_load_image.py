#resmi çalışma ortamına getirmek için resmin yolunu(dizinini) eklemeliyiz.
import cv2 as cv
path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"


#imread = resim okuma metodudur. ilgili resmin dizinini ister.
img = cv.imread(path + "mononoke.jpg")


print(type(img))
#img'in 'nump.ndarray' türünde olduğunu söyler. Yani fotoğraf üzerinde sayısal işlemler yapabiliriz.


#namedWindow = resmin adresini tuttuk şimdi bu resmi pencerede tutmalıyız
# window_autosize = fotoğrafın orijinal boyutlarıyla gösterilmesini sağar.
cv.namedWindow("opencv_test" , cv.WINDOW_AUTOSIZE) #pencerede tuttuk daha göstermiyoruz


#imshow = fotoğrafı ekranda gösterir
cv.imshow("opencv_test", img)
cv.waitKey(2000)
#0 = geçici bellekte sürekli yer tutar
#pozitif sayı girilirse ekranda gösterileceği milisaniyeyi verir ve ekrana eksi halini yazar


#açıktaki tüm pencereleri kapatır
cv.destroyAllWindows()