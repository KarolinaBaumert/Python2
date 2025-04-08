import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

brightened_image = cv2.add(gray, 50)  # Zwiększamy jasność każdego piksela

_, otsu_thresh = cv2.threshold(brightened_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Obraz rozjaśniony - Progowanie Otsu", otsu_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
