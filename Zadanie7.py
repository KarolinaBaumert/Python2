import cv2
import numpy as np

image = cv2.imread('image.jpg')

if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

s_lower = np.clip(s - 50, 0, 255)

s_higher = np.clip(s + 50, 0, 255)

hsv_lower = cv2.merge([h, s_lower, v])
hsv_higher = cv2.merge([h, s_higher, v])

image_lower = cv2.cvtColor(hsv_lower, cv2.COLOR_HSV2BGR)
image_higher = cv2.cvtColor(hsv_higher, cv2.COLOR_HSV2BGR)

cv2.imshow("Oryginalny obraz", image)
cv2.imshow("Obnizone nasycenie", image_lower)
cv2.imshow("Podwyzszone nasycenie", image_higher)
cv2.waitKey(0)
cv2.destroyAllWindows()
