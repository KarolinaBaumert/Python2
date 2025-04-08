import cv2
import numpy as np

obraz = cv2.imread('blue.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    B, G, R = cv2.split(obraz)

    zamieniony = cv2.merge([R, B, G])
    bez_czerwonego = cv2.merge([B, G, np.zeros_like(R)])

    cv2.imshow("Zamiana kanałów (R, B, G)", zamieniony)
    cv2.imshow("Bez czerwonego", bez_czerwonego)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
