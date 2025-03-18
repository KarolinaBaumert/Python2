import cv2
import imutils

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    nowa_szerokosc = 500
    przeskalowany = imutils.resize(obraz, width=nowa_szerokosc)

    cv2.imshow('Przeskalowany obraz', przeskalowany)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
