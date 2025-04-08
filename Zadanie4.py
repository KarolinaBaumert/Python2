import cv2
import numpy as np

image = cv2.imread('image.jpg')

if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

h = (h.astype(int) + 30) % 180
h = h.astype(np.uint8)

hsv_shifted = cv2.merge([h, s, v])
image_shifted = cv2.cvtColor(hsv_shifted, cv2.COLOR_HSV2BGR)

cv2.imshow('Oryginalny obraz', image)
cv2.imshow('Zmieniony odcień (H+30)', image_shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
