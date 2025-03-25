import cv2
import numpy as np

logo = cv2.imread('logo.jpg')

if logo is None:
    print("Nie udało się załadować logo!")
else:
    B, G, R = cv2.split(logo)

    zamiana = cv2.merge([R, G, B])
    bez_niebieskiego = cv2.merge([np.zeros_like(B), G, R])

    cv2.imshow("Zamiana B z R", zamiana)
    cv2.imshow("Bez niebieskiego", bez_niebieskiego)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
