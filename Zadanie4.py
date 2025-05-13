import cv2
import numpy as np

obraz = cv2.imread('Fanta.jpg')
szablon = cv2.imread('fanta_logo.jfif')
h, w = szablon.shape[:2]

metody = [
    ('TM_CCOEFF', cv2.TM_CCOEFF),
    ('TM_CCOEFF_NORMED', cv2.TM_CCOEFF_NORMED),
    ('TM_CCORR', cv2.TM_CCORR),
    ('TM_CCORR_NORMED', cv2.TM_CCORR_NORMED),
    ('TM_SQDIFF', cv2.TM_SQDIFF),
    ('TM_SQDIFF_NORMED', cv2.TM_SQDIFF_NORMED)
]

for nazwa, metoda in metody:
    kopia = obraz.copy()

    wynik = cv2.matchTemplate(kopia, szablon, metoda)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)

    if metoda in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        dopasowanie = min_val
    else:
        top_left = max_loc
        dopasowanie = max_val

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(kopia, top_left, bottom_right, (0, 0, 255), 2)

    print(f"[{nazwa}] Dopasowanie: {dopasowanie:.4f}  Współrzędne: {top_left}")
    cv2.imshow(nazwa, kopia)

cv2.waitKey(0)
cv2.destroyAllWindows()
