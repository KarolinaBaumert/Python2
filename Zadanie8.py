import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    (wysokosc, szerokosc) = obraz.shape[:2]
    center = (szerokosc // 2, wysokosc // 2)

    M1 = cv2.getRotationMatrix2D(center, 30, 1)
    obraz_obrocony_30 = cv2.warpAffine(obraz, M1, (szerokosc, wysokosc))

    M2 = cv2.getRotationMatrix2D(center, 30, 1)
    obraz_obrocony_60 = cv2.warpAffine(obraz_obrocony_30, M2, (szerokosc, wysokosc))

    M3 = cv2.getRotationMatrix2D(center, 30, 1)
    obraz_obrocony_90 = cv2.warpAffine(obraz_obrocony_60, M3, (szerokosc, wysokosc))

    M4 = cv2.getRotationMatrix2D(center, 90, 1)
    obraz_obrocony_90_single = cv2.warpAffine(obraz, M4, (szerokosc, wysokosc))

    cv2.imshow('Obraz po trzech obrotach po 30 stopni', obraz_obrocony_90)
    cv2.imshow('Obraz po jednym obrocie o 90 stopni', obraz_obrocony_90_single)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
