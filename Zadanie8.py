import cv2
import numpy as np

image = cv2.imread("kostka-brukowa.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

T = 100
_, binary_basic = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

_, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary_blurred = cv2.threshold(blurred, T, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(binary_blurred, kernel, iterations=1)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Progowanie podstawowe (T=100)", binary_basic)
cv2.imshow("Progowanie Otsu", binary_otsu)
cv2.imshow("Rozmycie + Progowanie (T=100)", binary_blurred)
cv2.imshow("Erozja po rozmyciu", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
