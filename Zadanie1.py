import cv2

sciezka_obraz = "image.jpg"
obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    wysokosc, szerokosc, _ = obraz.shape
    srodek_x, srodek_y = szerokosc // 2, wysokosc // 2
    prawy_dolny_x, prawy_dolny_y = szerokosc - 1, wysokosc - 1

    cv2.line(obraz, (srodek_x, srodek_y), (prawy_dolny_x, prawy_dolny_y), (255, 0, 0), 2)

    cv2.imshow("Obraz z linią", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
