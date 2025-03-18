import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

obraz_filtr = obraz.copy()
obraz_filtr[:, :, 2] = np.clip(obraz_filtr[:, :, 2] + 30, 0, 255)  # Czerwony +30
obraz_filtr[:, :, 1] = np.clip(obraz_filtr[:, :, 1] - 20, 0, 255)  # Zielony -20
obraz_filtr[:, :, 0] = np.clip(obraz_filtr[:, :, 0] + 10, 0, 255)  # Niebieski +10

cv2.imshow('Original', obraz)
cv2.imshow('Instagram Filter', obraz_filtr)

cv2.waitKey(0)
cv2.destroyAllWindows()
