#Googlenet modeli ile görüntü sınıflandırma

import cv2 as cv
import numpy as np

bin_model = "/Users/bahriyeisgor/Desktop/OpenCV/model/bvlc_googlenet.caffemodel"
protxt = "/Users/bahriyeisgor/Desktop/OpenCV/model/prototxt/deploy.prototxt"

net = cv.dnn.readNet(bin_model, protxt)

layer_names = net.getLayerNames()
"""
for name in layer_names:
    id = net.getLayerNames(name)
    layer = net.getLayer(id)
    print(f"layer id: {id}, type: {layer.type}, name: {layer.name}")
"""

for i in range(len(layer_names)):
    layer_id = net.getLayerId(layer_names[i])
    layer = net.getLayer(layer_id)
    print(f"Katman ID: {layer_id}, türü: {layer.type}, ismi: {layer_names[i]}")


with open("/Users/bahriyeisgor/Desktop/OpenCV/classification_classes_ILSVRC2012.txt", "rt") as f:
    classes = f.read().split('/n')

net = cv.dnn.readNetFromCaffe(bin_model, protxt)

image = cv.imread("/Users/bahriyeisgor/Desktop/OpenCV/images/goldfish.jpeg")

blob = cv.dnn.bloblFromImage(image, 1.0, (224, 224), (104, 117, 123), False, crop=False)

result = np.copy(image)

net.setInput(blob)
out = net.forward()

out = out.flatten()

classId = np.argmax(out)

confidence = out[classId]

t, _ = net.getPerfProfile()
label = 'cost time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

label = '%s: %4f' % (classes[classId] if classes else 'Class#%d' % classId, confidence)
cv.putText(result, label, (0, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

show_img = np.hstack((image, result))
cv.namedWindow("demo", cv.WINDOW_NORMAL)
cv.imshow("demo", show_img)
cv.waitKey(1000)

