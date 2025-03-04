import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    wysokosc, szerokosc, _ = obraz.shape

    wysokosc_podzialu = wysokosc // 3
    szerokosc_podzialu = szerokosc // 3

    x_start = szerokosc_podzialu
    y_start = wysokosc_podzialu

    fragment_srodek = obraz[y_start:y_start + wysokosc_podzialu, x_start:x_start + szerokosc_podzialu]

    cv2.imshow("Fragment środka obrazu", fragment_srodek)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
