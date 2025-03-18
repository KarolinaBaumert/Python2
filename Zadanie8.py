import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    powiekszony_cubic = cv2.resize(obraz, (obraz.shape[1] * 4, obraz.shape[0] * 4), interpolation=cv2.INTER_CUBIC)
    powiekszony_lanczos = cv2.resize(obraz, (obraz.shape[1] * 4, obraz.shape[0] * 4), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('Powiększony obraz (INTER_CUBIC)', powiekszony_cubic)
    cv2.imshow('Powiększony obraz (INTER_LANCZOS4)', powiekszony_lanczos)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
