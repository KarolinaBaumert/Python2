import cv2

image = cv2.imread("image.jpg")
if image is None:
    print("Błąd wczytywania obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresh_no_blur = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

_, thresh_with_blur = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Oryginalny obraz (szarość)", gray)
cv2.imshow("Obraz po rozmyciu Gaussa", blurred)
cv2.imshow("Progowanie bez rozmycia", thresh_no_blur)
cv2.imshow("Progowanie po rozmyciu", thresh_with_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
