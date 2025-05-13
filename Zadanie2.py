import cv2
import imutils

butelka = cv2.imread('Fanta.jpg')
logo = cv2.imread('fanta_logo.jfif')

if butelka is None or logo is None:
    print("Nie udało się wczytać obrazów.")
    exit()

def sprawdz_dopasowanie(obraz, kat_obrotu):
    obrocony = imutils.rotate(obraz, kat_obrotu)

    wynik = cv2.matchTemplate(obrocony, logo, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)

    h, w = logo.shape[:2]
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(obrocony, top_left, bottom_right, (0, 0, 255), 2)

    print(f"Obrót: {kat_obrotu}°, maxVal: {max_val:.4f}")
    cv2.imshow(f'Obrót {kat_obrotu}°', obrocony)

sprawdz_dopasowanie(butelka, 30)
sprawdz_dopasowanie(butelka, 45)

cv2.waitKey(0)
cv2.destroyAllWindows()
