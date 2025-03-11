import cv2
import numpy as np

obraz = np.zeros((300, 300, 3), dtype=np.uint8)

srodek = (150, 150)

cv2.rectangle(obraz, (100, 100), (200, 200), (0, 255, 0), -1)
cv2.circle(obraz, srodek, 30, (0, 0, 255), -1)

cv2.imshow("Złożona figura", obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
