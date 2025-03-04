import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    wysokosc, szerokosc, _ = obraz.shape

    pol_wysokosci = wysokosc // 2
    pol_szerokosci = szerokosc // 2

    obraz[0:pol_wysokosci, 0:pol_szerokosci] = [255, 0, 0]

    cv2.imshow("Obraz po zmianach", obraz)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
