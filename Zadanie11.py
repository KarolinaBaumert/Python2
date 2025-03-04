import cv2
import numpy as np

sciezka_obraz = "image.jpg"

obraz = cv2.imread(sciezka_obraz)

if obraz is None:
    print(f"Nie znaleziono pliku: {sciezka_obraz}")
else:
    obraz_hsv = cv2.cvtColor(obraz, cv2.COLOR_BGR2HSV)

    jasnosc = obraz_hsv[:, :, 2]

    max_jasnosc = np.max(jasnosc)
    wspolrzedne = np.unravel_index(np.argmax(jasnosc), jasnosc.shape)

    print(f"Współrzędne piksela o najwyższej jasności: {wspolrzedne}")
    print(f"Najwyższa wartość jasności: {max_jasnosc}")

    cv2.imshow("Obraz", obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
