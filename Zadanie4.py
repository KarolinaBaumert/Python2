import cv2

image = cv2.imread("strona.jpg")
if image is None:
    print("Błąd wczytywania obrazu!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               blockSize=21,
                               C=10)

cv2.imshow("Oryginalny", image)
cv2.imshow("Binarna segmentacja tekstu", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
