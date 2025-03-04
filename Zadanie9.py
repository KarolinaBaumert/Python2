import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    cv2.imshow("Obraz przed", obraz)

    obraz[50:100, 50:100] = [255, 255, 255]

    cv2.imshow("Obraz po", obraz)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
