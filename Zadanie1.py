import cv2
import numpy as np

shape1 = np.zeros((300, 300), dtype="uint8")
shape2 = np.zeros((300, 300), dtype="uint8")

pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(shape1, [pts], 255)

cv2.circle(shape2, (150, 150), 100, 255, -1)

bitwise_and = cv2.bitwise_and(shape1, shape2)
bitwise_or = cv2.bitwise_or(shape1, shape2)
bitwise_xor = cv2.bitwise_xor(shape1, shape2)
bitwise_not = cv2.bitwise_not(shape1)

cv2.imshow("Triangle", shape1)
cv2.imshow("Circle", shape2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("XOR", bitwise_xor)
cv2.imshow("NOT (Triangle)", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
