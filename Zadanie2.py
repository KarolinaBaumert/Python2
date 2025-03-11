import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    (wysokosc, szerokosc) = obraz.shape[:2]
    center = (szerokosc // 2, wysokosc // 2)
    M = cv2.getRotationMatrix2D(center, -90, 1)
    obraz_obrocony = cv2.warpAffine(obraz, M, (szerokosc, wysokosc))

    cv2.imshow('Obraz po obrocie o -90 stopni', obraz_obrocony)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
