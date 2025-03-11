import cv2
import numpy as np

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    tx = int(input("Podaj wartość przesunięcia w poziomie (tx): "))
    ty = int(input("Podaj wartość przesunięcia w pionie (ty): "))

    M = np.float32([[1, 0, tx], [0, 1, ty]])

    obraz_przesuniety = cv2.warpAffine(obraz, M, (obraz.shape[1], obraz.shape[0]))

    cv2.imshow('Obraz po przesunięciu', obraz_przesuniety)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
