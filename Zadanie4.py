import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    startX = int(input("Podaj startX: "))
    endX = int(input("Podaj endX: "))
    startY = int(input("Podaj startY: "))
    endY = int(input("Podaj endY: "))

    roi = obraz[startY:endY, startX:endX]

    cv2.imshow("Przycięty Obraz", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
