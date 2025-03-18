import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    nowy_rozmiar = (200, 300)
    zmieniony_obraz = cv2.resize(obraz, nowy_rozmiar)

    cv2.imshow('Obraz 200x300', zmieniony_obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
