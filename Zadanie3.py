import cv2

original = cv2.imread('kostka-brukowa.jpg')
if original is None:
    print("Nie można załadować obrazu.")
    exit()

scales = [100, 50, 25]

for scale in scales:
    width = int(original.shape[1] * scale / 100)
    height = int(original.shape[0] * scale / 100)
    resized = cv2.resize(original, (width, height))

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contour_img = resized.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 2)

    print(f"Skala: {scale}% - Liczba konturów: {len(contours)}")
    cv2.imshow(f'Kontury - {scale}%', contour_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
