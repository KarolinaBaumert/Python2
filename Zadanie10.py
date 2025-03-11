import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    (wysokosc, szerokosc) = obraz.shape[:2]
    center = (szerokosc // 2, wysokosc // 2)

    for kąt in range(0, 360, 15):
        M = cv2.getRotationMatrix2D(center, kąt, 1)
        obraz_obrocony = cv2.warpAffine(obraz, M, (szerokosc, wysokosc))

        cv2.imshow(f'Obraz obrócony o {kąt} stopni', obraz_obrocony)

        cv2.waitKey(500)

    cv2.destroyAllWindows()
