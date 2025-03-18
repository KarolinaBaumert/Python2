import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    for skala in np.arange(1.0, 3.2, 0.2):
        nowa_szerokosc = int(obraz.shape[1] * skala)
        nowa_wysokosc = int(obraz.shape[0] * skala)
        zmieniony_rozmiar = cv2.resize(obraz, (nowa_szerokosc, nowa_wysokosc), interpolation=cv2.INTER_LINEAR)

        cv2.imshow('Dynamiczna zmiana rozmiaru', zmieniony_rozmiar)
        cv2.waitKey(500)

    cv2.destroyAllWindows()
