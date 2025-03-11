import cv2
import numpy as np

obraz = np.zeros((300, 300, 3), dtype=np.uint8)

cv2.circle(obraz, (40, 40), 40, (255, 0, 0), -1)
cv2.circle(obraz, (150, 150), 60, (0, 0, 255), -1)

cv2.imshow("Okręgi", obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
