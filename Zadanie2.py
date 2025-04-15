import cv2

image = cv2.imread("kostka_brukowa1.jpg")
if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

block_sizes = [11, 21, 31, 41]

for bsize in block_sizes:
    thresh = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, bsize, 5)
    cv2.imshow(f"blockSize = {bsize}", thresh)

cv2.imshow("Oryginalny", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
