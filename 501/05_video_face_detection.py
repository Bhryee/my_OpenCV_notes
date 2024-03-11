import cv2 as cv
#modelin katmanlarının ağırlıklarının bilgilerinin olduğu dosya
bin_model = "/Users/bahriyeisgor/Desktop/OpenCV/model/bvlc_googlenet.caffemodel"

#model mimarisine ilişkin katmanlarla ilgili bilgilerin olduğu dosya
protxt = "/Users/bahriyeisgor/Desktop/OpenCV/model/prototxt/deploy.prototxt"

net = cv.dnn.readNet(bin_model, protxt)

net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_BACKEND_OPENCV)

cap = cv.VideoCapture("video_path")
while True:
    ret, image = cap.read()
    image = cv.flip(image, 1)
    if ret is False:
        break
    h, w = image.shape[:2]
    blobImage = cv.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), False, False)
    net.setInput(blobImage)
    cvOut = net.forward()

    for detection in cvOut[0, 0, :, :]:
        score = float(detection [2])
        objIndex = int(detection[1])
        if score > 0.5:
            left = detection [3] * w
            top = detection [4] * h 
            right = detection [5] * w
            bottom = detection[6] * h
            cv.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness=2)
            cv.putText(image, "score:%.2f" % score, (int(left), int(top)),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    cv.imshow('video-ssd-demo', frame)
    c = cv.waitkey(10)
    if c == 27:
        break