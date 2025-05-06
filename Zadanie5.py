import cv2

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

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

    label = f"{w}x{h} px"
    cv2.putText(resized, label, (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.imshow('Pomiar wymiarów kostek', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
