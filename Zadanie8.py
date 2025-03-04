import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    cv2.imshow("Obraz przed", obraz)

    obraz[99, :] = [0, 255, 0]

    cv2.imshow("Obraz po", obraz)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
