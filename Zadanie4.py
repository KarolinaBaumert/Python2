import cv2

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    wysokosc, szerokosc, _ = obraz.shape

    try:
        x = int(input(f"Podaj współrzędną x (0 - {szerokosc - 1}): "))
        y = int(input(f"Podaj współrzędną y (0 - {wysokosc - 1}): "))

        if x < 0 or x >= szerokosc or y < 0 or y >= wysokosc:
            print("Podane współrzędne są poza zakresem obrazu!")
        else:
            obraz[y, x] = [0, 0, 0]

            cv2.imshow("Zmodyfikowany obraz", obraz)

            cv2.waitKey(0)

            cv2.destroyAllWindows()

    except ValueError:
        print("Wprowadź poprawne liczby całkowite!")
