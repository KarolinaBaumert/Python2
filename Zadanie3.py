import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    szerokosc = obraz.shape[1]
    prawa_polowa = obraz[:, szerokosc//2:]
    cv2.imshow('Prawa Polowa', prawa_polowa)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
