import cv2 as cv
#modelin katmanlarının ağırlıklarının bilgilerinin olduğu dosya
bin_model = ".../bvlc_googlenet.caffemodel"

#model mimarisine ilişkin katmanlarla ilgili bilgilerin olduğu dosya
protxt = ".../deploy.prototxt"

cap = cv.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    h, w = frame.shape[:2]
    blobImage = cv.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False)
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
            cv.putText(image, "score:%.2f, %s" % (score, ObjName[objIndex]),
                       (int(left) - 10, int(top) - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8)
    
    cv.imshow('video-ssd-demo', frame)
    c = cv.waitkey(1)
    if c == 27:
        break

    
