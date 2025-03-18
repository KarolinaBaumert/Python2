import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    zmniejszony_obraz = cv2.resize(obraz, (obraz.shape[1] // 2, obraz.shape[0] // 2))

    cv2.imshow('Zmniejszony obraz', zmniejszony_obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
