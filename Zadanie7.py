import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

masked_image = cv2.bitwise_and(image, image, mask=otsu_thresh)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Binarna maska (Otsu)", otsu_thresh)
cv2.imshow("Obiekt po wycięciu", masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
