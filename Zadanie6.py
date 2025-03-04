import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    wysokosc, szerokosc, _ = obraz.shape

    srodek_x = szerokosc // 2
    srodek_y = wysokosc // 2

    kwadrat_wielkosc = 100

    x_start = srodek_x - kwadrat_wielkosc // 2
    y_start = srodek_y - kwadrat_wielkosc // 2

    obraz[y_start:y_start+kwadrat_wielkosc, x_start:x_start+kwadrat_wielkosc] = [0, 0, 255]

    cv2.imshow("Obraz po zmianach", obraz)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
