import cv2

sciezka = "image.jfif"

obraz = cv2.imread(sciezka, cv2.IMREAD_GRAYSCALE)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka}")
else:
    if len(obraz.shape) == 2:
        liczba_kanalow = 1
    else:
        liczba_kanalow = obraz.shape[2]

    print(f"Liczba kanałów w obrazie: {liczba_kanalow}")
