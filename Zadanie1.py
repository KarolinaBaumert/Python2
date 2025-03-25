import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    B, G, R = cv2.split(obraz)

    cv2.imwrite("blue_channel.jpg", B)
    cv2.imwrite("green_channel.jpg", G)
    cv2.imwrite("red_channel.jpg", R)

    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
