import cv2
import imutils
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    cv2.imshow('Oryginalny Obraz', obraz)

    obraz_imutils = imutils.translate(obraz, x=100, y=50)

    M = np.float32([[1, 0, 100], [0, 1, 50]])
    obraz_cv2 = cv2.warpAffine(obraz, M, (obraz.shape[1], obraz.shape[0]))

    cv2.imshow('Obraz po przesunięciu (imutils)', obraz_imutils)
    cv2.imshow('Obraz po przesunięciu (cv2)', obraz_cv2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
