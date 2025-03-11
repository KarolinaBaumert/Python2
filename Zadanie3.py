import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    cv2.imshow('Oryginalny Obraz', obraz)

    szerokosc, wysokosc = obraz.shape[1], obraz.shape[0]

    M = np.float32([[1, 0, szerokosc // 2], [0, 1, wysokosc // 2]])

    obraz_przesuniety = cv2.warpAffine(obraz, M, (obraz.shape[1], obraz.shape[0]))

    cv2.imshow('Obraz po przesunięciu', obraz_przesuniety)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
