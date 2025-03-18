import cv2

obraz = cv2.imread('image.jpg')

wysokosc, szerokosc, _ = obraz.shape
startX = 0
endX = 100
startY = 0
endY = 100

przesuniecie = 10

while True:
    roi = obraz[startY:endY, startX:endX]
    cv2.imshow('ROI', roi)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('d'):
        startX += przesuniecie
        endX += przesuniecie

    elif key == ord('a'):
        startX -= przesuniecie
        endX -= przesuniecie

    elif key == ord('q'):
        break

cv2.destroyAllWindows()
