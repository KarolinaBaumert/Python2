import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

otsu_threshold = _

plt.figure(figsize=(10, 5))
plt.plot(hist)
plt.title('Histogram obrazu w skali szarości')
plt.xlabel('Wartości intensywności')
plt.ylabel('Częstotliwość')
plt.axvline(x=otsu_threshold, color='r', linestyle='--', label=f'Otsu threshold = {otsu_threshold}')
plt.legend(loc='upper right')
plt.show()

cv2.imshow("Obraz po progowaniu Otsu", otsu_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
