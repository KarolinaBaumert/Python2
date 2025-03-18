import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

obraz_numpy = np.clip(obraz + 150, 0, 255).astype(np.uint8)

obraz_cv2 = cv2.add(obraz, (150, 150, 150, 0))

cv2.imshow('Original', obraz)
cv2.imshow('Brightness Increase with NumPy', obraz_numpy)
cv2.imshow('Brightness Increase with cv2.add()', obraz_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
