import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

obraz_numpy = np.clip(obraz - 80, 0, 255).astype(np.uint8)

obraz_cv2 = cv2.subtract(obraz, (80, 80, 80, 0))

cv2.imshow('Original', obraz)
cv2.imshow('Dimmed with NumPy', obraz_numpy)
cv2.imshow('Dimmed with cv2.subtract()', obraz_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
