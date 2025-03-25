import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    B, G, R = cv2.split(obraz)

    R = cv2.add(R, 50)

    wzmocniony = cv2.merge([B, G, R])

    cv2.imshow("Obraz po wzmocnieniu czerwieni", wzmocniony)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
