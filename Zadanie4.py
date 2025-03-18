import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    skala = 3
    metody = {
        'INTER_NEAREST': cv2.INTER_NEAREST,
        'INTER_LINEAR': cv2.INTER_LINEAR,
        'INTER_CUBIC': cv2.INTER_CUBIC,
        'INTER_LANCZOS4': cv2.INTER_LANCZOS4
    }

    for nazwa, metoda in metody.items():
        powiekszony = cv2.resize(obraz, None, fx=skala, fy=skala, interpolation=metoda)
        cv2.imshow(nazwa, powiekszony)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
