import cv2

obraz = cv2.imread('image.jpg')

fragment = obraz[50:150, 50:150]

obraz[250:350, 250:350] = fragment

cv2.imshow("Wynik", obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
