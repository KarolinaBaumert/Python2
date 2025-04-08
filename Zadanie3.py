import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh_with_blur = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)  # Struktura elementu (np. 3x3)
eroded_image = cv2.erode(thresh_with_blur, kernel, iterations=1)

cv2.imshow("Obraz przed erozją", thresh_with_blur)
cv2.imshow("Obraz po erozji", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
