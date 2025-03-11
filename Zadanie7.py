import cv2
import imutils
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    (wysokosc, szerokosc) = obraz.shape[:2]
    center = (szerokosc // 2, wysokosc // 2)
    M = cv2.getRotationMatrix2D(center, 60, 1)
    obraz_obrocony_warpAffine = cv2.warpAffine(obraz, M, (szerokosc, wysokosc))

    obraz_obrocony_imutils = imutils.rotate(obraz, 60)

    cv2.imshow('Obraz po obrocie o 60 stopni (cv2.warpAffine)', obraz_obrocony_warpAffine)
    cv2.imshow('Obraz po obrocie o 60 stopni (imutils.rotate)', obraz_obrocony_imutils)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
