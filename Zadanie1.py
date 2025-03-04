import cv2

sciezka = "image.jfif"

obraz = cv2.imread(sciezka)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka}")
else:
    cv2.imshow("Obraz", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()