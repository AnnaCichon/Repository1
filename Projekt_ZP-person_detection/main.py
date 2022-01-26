import cv2
from program.person_detection import detection
import time
import glob


if __name__ == '__main__':

    for image in glob.glob("images/*.jpg"):
        image = cv2.imread(image)
        start_time = time.time()
        print(detection(image))
        print("- %.3f sekund " % (time.time() - start_time))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
