#Görüntüye gürültü ekleme işlemi

import cv2 as cv
import numpy as np
src = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/foto.jpg")

def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 1000

    #0'dan h bilgisine göre nums kadar rastgele sayılar oluşturur.
    rows = np.random.randint(0, h, nums, dtype=int)
    cols = np.random.randint(0, w, nums, dtype=int)

    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255) #seçilen piksellere beyaz eklemeler yapar
        else:
            image[rows[i], cols[i]] = (0, 0, 0) #seçilen piksellere siyah eklemeler yapar
    return image

h, w = src.shape[:2]

copy = np.copy(src)
copy = add_salt_pepper_noise(copy)

result = np.zeros([h, w * 2, 3], dtype = src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = copy

cv.imshow("Result", result)
cv.waitKey(0)
cv.destroyAllWindows()