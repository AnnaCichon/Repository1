import numpy as np
import cv2
import imutils
from imutils.object_detection import non_max_suppression

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detection(image):
    image = imutils.resize(image, width=600)
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    selection = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    person = 0
    for (xA, yA, xB, yB) in selection:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
        person += 1

    cv2.putText(image, f'Ilosc osob : {person}', (40, 50),
                cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow("Wyszukiwanie osob", image)
    return f'Ilosc osob : {person}'
