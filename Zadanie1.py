import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

obraz_numpy = np.clip(obraz + 50, 0, 255).astype(np.uint8)

obraz_opencv = cv2.convertScaleAbs(obraz, alpha=1, beta=50)

cv2.imshow('Original', obraz)
cv2.imshow('Brightness Increase with NumPy', obraz_numpy)
cv2.imshow('Brightness Increase with OpenCV', obraz_opencv)

cv2.waitKey(0)
cv2.destroyAllWindows()
