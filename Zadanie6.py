import cv2
import imutils

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    nowa_wysokosc = 400
    przeskalowany = imutils.resize(obraz, height=nowa_wysokosc)

    cv2.imshow('Przeskalowany obraz', przeskalowany)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
