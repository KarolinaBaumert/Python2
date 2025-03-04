import cv2

sciezka_obraz1 = "image.jfif"
sciezka_obraz2 = "szary_image.jpg"


obraz1 = cv2.imread(sciezka_obraz1)
obraz2 = cv2.imread(sciezka_obraz2)

if obraz1 is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz1}")
else:
    cv2.imshow("Obraz 1", obraz1)

if obraz2 is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz2}")
else:
    cv2.imshow("Obraz 2", obraz2)

cv2.waitKey(0)

cv2.destroyAllWindows()
