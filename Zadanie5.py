import cv2

image = cv2.imread("elementy.jpg")
if image is None:
    print("Nie znaleziono obrazu!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV,
                               blockSize=21,
                               C=10)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

roi = cv2.bitwise_and(image, image, mask=cleaned)

cv2.imshow("Oryginalny", image)
cv2.imshow("Maska ROI", cleaned)
cv2.imshow("Obiekty (ROI)", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
