import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    wysokosc = obraz.shape[0]
    dolna_polowa = obraz[wysokosc//2:, :]
    cv2.imshow('Dolna Polowa', dolna_polowa)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
