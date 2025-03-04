import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    piksel_1 = obraz[50, 50]
    piksel_2 = obraz[200, 200]

    print(f"Wartości piksela w (50, 50): B = {piksel_1[0]}, G = {piksel_1[1]}, R = {piksel_1[2]}")
    print(f"Wartości piksela w (200, 200): B = {piksel_2[0]}, G = {piksel_2[1]}, R = {piksel_2[2]}")

    roznica_b = piksel_1[0] - piksel_2[0]
    roznica_g = piksel_1[1] - piksel_2[1]
    roznica_r = piksel_1[2] - piksel_2[2]

    print(f"Różnica w B: {roznica_b}")
    print(f"Różnica w G: {roznica_g}")
    print(f"Różnica w R: {roznica_r}")
