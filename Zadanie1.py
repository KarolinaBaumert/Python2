import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    roi = obraz[0:100, 0:100]
    cv2.imshow('ROI', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
