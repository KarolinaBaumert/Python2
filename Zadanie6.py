import cv2
import numpy as np

scene = cv2.imread('klocki.jpg')
template = cv2.imread('klocek.jpg')
h, w = template.shape[:2]

result = cv2.matchTemplate(scene, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(scene, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("Detekcja wielu szablonów", scene)
cv2.waitKey(0)
cv2.destroyAllWindows()
