import cv2

butelka = cv2.imread('Fanta.jpg')
logo = cv2.imread('fanta_logo.jfif')

if butelka is None or logo is None:
    print("Nie udało się wczytać obrazów.")
    exit()

wynik = cv2.matchTemplate(butelka, logo, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)

h, w = logo.shape[:2]

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(butelka, top_left, bottom_right, (0, 0, 255), 2)

print(f"Pozycja wykrytego logo: {top_left}")
print(f"Wartość dopasowania (maxVal): {max_val:.4f}")

cv2.imshow('Wykryte logo', butelka)
cv2.waitKey(0)
cv2.destroyAllWindows()
