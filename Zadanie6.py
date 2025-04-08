import cv2
import numpy as np

image = cv2.imread('person.jpg')

if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_skin, upper_skin)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Maska skóry", mask)
cv2.imshow("Obszary skóry", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
