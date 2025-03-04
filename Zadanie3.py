import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    wysokosc, szerokosc, _ = obraz.shape
    srodek_x = szerokosc // 2
    srodek_y = wysokosc // 2

    pixel_srodek = obraz[srodek_y, srodek_x]

    blue = pixel_srodek[0]
    green = pixel_srodek[1]
    red = pixel_srodek[2]

    print(f"Współrzędne środka obrazu: ({srodek_x}, {srodek_y})")
    print(f"Składowe koloru piksela w środku (BGR): R: {red}, G: {green}, B: {blue}")
