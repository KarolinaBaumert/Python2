import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    zmniejszony = cv2.resize(obraz, (obraz.shape[1] // 5, obraz.shape[0] // 5), interpolation=cv2.INTER_AREA)

    cv2.imshow('Zmniejszony obraz (INTER_AREA)', zmniejszony)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
