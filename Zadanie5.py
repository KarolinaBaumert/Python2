import cv2
import imutils

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    obraz_obrocony = imutils.rotate(obraz, 180)

    cv2.imshow('Obraz po obrocie o 180 stopni', obraz_obrocony)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
