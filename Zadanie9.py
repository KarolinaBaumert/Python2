import cv2

obraz = cv2.imread('image.jpg')

przyciety_obraz = obraz[0:300, 0:300]

cv2.imwrite('cropped_image.jpg', przyciety_obraz)

cv2.imshow('Cropped Image', przyciety_obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
