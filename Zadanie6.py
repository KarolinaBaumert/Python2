import cv2

sciezka_obraz = "image.jfif"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)

    cv2.imshow("Obraz", obraz)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
