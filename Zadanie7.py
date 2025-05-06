import cv2
import numpy as np

img = cv2.imread('kostka-brukowa.jpg')
if img is None:
    print("Nie można wczytać obrazu.")
    exit()

scale_width = 300
scale_factor = scale_width / img.shape[1]
dim = (scale_width, int(img.shape[0] * scale_factor))
resized = cv2.resize(img, dim)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

filtered_contours = []
widths = []
heights = []

for cnt in contours:
    area = cv2.contourArea(cnt)
    if 500 < area < 5000:
        x, y, w, h = cv2.boundingRect(cnt)
        widths.append(w)
        heights.append(h)
        filtered_contours.append(cnt)
        cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(resized, f"{w}x{h}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

if widths and heights:
    avg_width = np.mean(widths)
    avg_height = np.mean(heights)
    min_size = f"{min(widths)}x{min(heights)}"
    max_size = f"{max(widths)}x{max(heights)}"
else:
    avg_width = avg_height = 0
    min_size = max_size = "0x0"

print(f"Liczba wykrytych kostek: {len(filtered_contours)}")
print(f"Średnia szerokość: {avg_width:.2f} px")
print(f"Średnia wysokość: {avg_height:.2f} px")
print(f"Minimalny rozmiar: {min_size}")
print(f"Maksymalny rozmiar: {max_size}")

cv2.imshow("Kostki z pomiarami", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
