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

_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

modes = {
    "RETR_EXTERNAL": cv2.RETR_EXTERNAL,
    "RETR_TREE": cv2.RETR_TREE,
    "RETR_LIST": cv2.RETR_LIST
}

for name, mode in modes.items():
    contour_image = resized.copy()

    contours, hierarchy = cv2.findContours(thresh, mode, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)

    cv2.imshow(f'Contours - {name}', contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
