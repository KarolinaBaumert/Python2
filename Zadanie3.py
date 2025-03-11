import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    (wysokosc, szerokosc) = obraz.shape[:2]
    M = cv2.getRotationMatrix2D((0, 0), 30, 1)
    obraz_obrocony = cv2.warpAffine(obraz, M, (szerokosc, wysokosc))

    cv2.imshow('Obraz po obrocie o 30 stopni względem lewego górnego narożnika', obraz_obrocony)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
