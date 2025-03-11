import cv2
import numpy as np

obraz = np.zeros((400, 400, 3), dtype=np.uint8)
srodek = (200, 200)

for i in range(20, 201, 20):
    cv2.rectangle(obraz, (srodek[0] - i // 2, srodek[1] - i // 2),
                  (srodek[0] + i // 2, srodek[1] + i // 2), (0, 255, 0), 2)

cv2.imshow("Kwadraty", obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
