import cv2
import imutils

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    nowy_obraz = imutils.resize(obraz, width=800)
    cv2.imwrite('resized_output.jpg', nowy_obraz)
    cv2.imshow('Powiekszony obraz', nowy_obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
