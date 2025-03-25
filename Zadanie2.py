import cv2

obraz = cv2.imread('logo.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    B, G, R = cv2.split(obraz)

    cv2.imshow("Oryginalny obraz", obraz)
    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
