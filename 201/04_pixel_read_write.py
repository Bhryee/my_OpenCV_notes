import cv2 as cv

path = "/Users/bahriyeisgor/Desktop/OpenCV/images/"
img = cv.imread(path + "mononoke.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)

h, w, ch = img.shape
#h = yükseklık
#w = genişlik
#ch = rgb

print("h,w,ch",h,w,ch)

for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = [b, g, r]

cv.imshow("output", img)
cv.waitKey(2000)
