import cv2

image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

image1 = cv2.resize(image1, (300, 300))
image2 = cv2.resize(image2, (300, 300))

difference = cv2.bitwise_xor(image1, image2)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("XOR Difference", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()
