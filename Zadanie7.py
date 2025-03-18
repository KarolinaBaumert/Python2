import cv2

obraz = cv2.imread('image.jpg')

wysokosc, szerokosc, _ = obraz.shape

wysokosc_czesc = wysokosc // 3
szerokosc_czesc = szerokosc // 3

czesci = []
for i in range(3):
    for j in range(3):
        czesc = obraz[i*wysokosc_czesc:(i+1)*wysokosc_czesc, j*szerokosc_czesc:(j+1)*szerokosc_czesc]
        czesci.append(czesc)

for i, czesc in enumerate(czesci):
    cv2.imshow(f"Czesc {i+1}", czesc)

cv2.waitKey(0)
cv2.destroyAllWindows()
