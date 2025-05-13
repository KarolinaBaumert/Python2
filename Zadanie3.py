import cv2

butelka = cv2.imread('Fanta.jpg')
logo = cv2.imread('fanta_logo.jfif')

def sprawdz_skalowanie(obraz, skala, nazwa):
    szerokosc = int(obraz.shape[1] * skala)
    wysokosc = int(obraz.shape[0] * skala)
    obraz_skalowany = cv2.resize(obraz, (szerokosc, wysokosc))

    wynik = cv2.matchTemplate(obraz_skalowany, logo, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)

    h, w = logo.shape[:2]
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(obraz_skalowany, top_left, bottom_right, (0, 255, 0), 2)

    print(f"[{nazwa}] Skala: {skala}, maxVal: {max_val:.4f}")
    cv2.imshow(nazwa, obraz_skalowany)

sprawdz_skalowanie(butelka, 0.8, "Pomniejszony o 20%")
sprawdz_skalowanie(butelka, 1.2, "Powiększony o 20%")

cv2.waitKey(0)
cv2.destroyAllWindows()
