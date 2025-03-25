import cv2
import numpy as np

obraz = cv2.imread('flowers.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    hsv = cv2.cvtColor(obraz, cv2.COLOR_BGR2HSV)

    dolny_zakres = np.array([35, 50, 50])
    gorny_zakres = np.array([85, 255, 255])

    maska = cv2.inRange(hsv, dolny_zakres, gorny_zakres)
    wynik = cv2.bitwise_and(obraz, obraz, mask=maska)

    cv2.imshow('Oryginalny Obraz', obraz)
    cv2.imshow('Maska', maska)
    cv2.imshow('Wynik Ekstrakcji Koloru', wynik)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
