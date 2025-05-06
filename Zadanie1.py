import cv2

image = cv2.imread('kostka-brukowa.jpg')
if image is None:
    print("Nie można załadować obrazu.")
    exit()

scale_percent = 300 / image.shape[1] * 100
width = 300
height = int(image.shape[0] * scale_percent / 100)
resized = cv2.resize(image, (width, height))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresholds = [100, 140, 180]

for t in thresholds:
    _, thresh_img = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    cv2.imshow(f'Threshold = {t}', thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
