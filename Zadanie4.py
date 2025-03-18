import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    odbicie_poziome = cv2.flip(obraz, 1)

    odbicie_pionowe = cv2.flip(obraz, 0)

    odbicie_both = cv2.flip(obraz, -1)

    cv2.imshow('Oryginał', obraz)
    cv2.imshow('Odbicie poziome', odbicie_poziome)
    cv2.imshow('Odbicie pionowe', odbicie_pionowe)
    cv2.imshow('Odbicie względem obu osi', odbicie_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
