import cv2
import numpy as np

obraz = cv2.imread('face.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    maska = np.zeros(obraz.shape[:2], dtype="uint8")
    (h, w) = obraz.shape[:2]
    cv2.ellipse(maska, (w // 2, h // 2), (w // 4, h // 3), 0, 0, 360, 255, -1)

    wynik = cv2.bitwise_and(obraz, obraz, mask=maska)

    cv2.imshow('Oryginalny Obraz', obraz)
    cv2.imshow('Maska', maska)
    cv2.imshow('Wynik Maskowania Twarzy', wynik)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
