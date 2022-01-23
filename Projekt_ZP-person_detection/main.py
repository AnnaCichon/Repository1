import cv2
from program.person_detection import detection
import time

if __name__ == '__main__':

    images = [cv2.imread('images/fot1.jpg'), cv2.imread('images/fot2.jpg'),
              cv2.imread('images/fot3.jpg'), cv2.imread('images/fot4.jpg')]

    for image in images:
        start_time = time.time()
        print(detection(image))
        print("--- %.3f sekund ---" % (time.time() - start_time))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
