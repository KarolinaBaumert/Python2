import cv2

sciezka_wejsciowa = "image.jfif"
sciezka_wyjsciowa = "szary_image.jpg"

obraz_szary = cv2.imread(sciezka_wejsciowa, cv2.IMREAD_GRAYSCALE)

if obraz_szary is None:
    print(f"Nie znaleziono pliku: {sciezka_wejsciowa}")
else:
    cv2.imwrite(sciezka_wyjsciowa, obraz_szary)
    print(f"Obraz zapisano jako: {sciezka_wyjsciowa}")
