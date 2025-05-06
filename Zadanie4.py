import cv2
import os

img = cv2.imread('kostka-brukowa.jpg')
if img is None:
    print("Nie można załadować obrazu.")
    exit()

scale_width = 300
scale_factor = scale_width / img.shape[1]
dim = (scale_width, int(img.shape[0] * scale_factor))
resized = cv2.resize(img, dim)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output_dir = 'kostki'
os.makedirs(output_dir, exist_ok=True)

for i, cnt in enumerate(contours, start=1):
    x, y, w, h = cv2.boundingRect(cnt)

    kostka = resized[y:y+h, x:x+w]
    filename = os.path.join(output_dir, f'kostka_{i:02d}.png')
    cv2.imwrite(filename, kostka)

    cx, cy = x + w // 2, y + h // 2
    cv2.putText(resized, str(i), (cx - 10, cy + 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow('Numerowane kostki', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
