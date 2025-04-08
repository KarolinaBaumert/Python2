import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

brightened_image = cv2.add(gray, 50)  # Zwiększamy jasność każdego piksela

_, thresh_original = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

_, thresh_brightened = cv2.threshold(brightened_image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Obraz oryginalny po progowaniu", thresh_original)
cv2.imshow("Obraz rozjaśniony po progowaniu", thresh_brightened)

cv2.waitKey(0)
cv2.destroyAllWindows()
