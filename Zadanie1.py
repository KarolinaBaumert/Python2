import cv2

image = cv2.imread("kostka_brukowa1.jpg")
if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh_simple = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

_, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

thresh_adapt_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 11, 5)

thresh_adapt_gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 11, 5)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Progowanie proste (T=100)", thresh_simple)
cv2.imshow("Progowanie Otsu", thresh_otsu)
cv2.imshow("Progowanie adaptacyjne - MEAN", thresh_adapt_mean)
cv2.imshow("Progowanie adaptacyjne - GAUSSIAN", thresh_adapt_gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
