import cv2

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
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 500 < area < 5000:
        filtered_contours.append(cnt)

output = resized.copy()
cv2.drawContours(output, filtered_contours, -1, (0, 0, 255), 2)

cv2.imshow('Kontury po filtracji', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
