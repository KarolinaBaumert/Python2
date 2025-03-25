import cv2
import numpy as np

obraz = cv2.imread('redcar.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    hsv = cv2.cvtColor(obraz, cv2.COLOR_BGR2HSV)

    dolna_czerwona = np.array([0, 120, 70])
    gorna_czerwona = np.array([10, 255, 255])

    maska = cv2.inRange(hsv, dolna_czerwona, gorna_czerwona)

    obraz[maska > 0] = obraz[maska > 0] + (0, 0, 50)

    cv2.imshow("Zwiększone nasycenie czerwonego", obraz)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
