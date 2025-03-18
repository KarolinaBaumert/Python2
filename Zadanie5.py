import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    wysokosc, szerokosc = obraz.shape[:2]
    x_start = szerokosc // 4
    x_end = szerokosc * 3 // 4
    y_start = wysokosc // 4
    y_end = wysokosc * 3 // 4

    fragment = obraz[y_start:y_end, x_start:x_end]

    odbicie_fragmentu = cv2.flip(fragment, -1)

    obraz[y_start:y_end, x_start:x_end] = odbicie_fragmentu

    cv2.imshow('Obraz po odbiciu fragmentu', obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
