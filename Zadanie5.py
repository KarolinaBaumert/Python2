import cv2

zrzut = cv2.imread('insta.jpg')
szablon = cv2.imread('lupa.jpg')
h, w = szablon.shape[:2]

wynik = cv2.matchTemplate(zrzut, szablon, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wynik)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(zrzut, top_left, bottom_right, (0, 255, 0), 2)

print(f"Dopasowanie (maxVal): {max_val:.4f}")
print(f"Współrzędne dopasowania: {top_left}")

cv2.imshow("Dopasowanie ikony", zrzut)
cv2.waitKey(0)
cv2.destroyAllWindows()
