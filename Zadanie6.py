import cv2

obraz = cv2.imread('image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    wybor = int(input("Podaj sposób odbicia:\n0 - odbicie pionowe\n1 - odbicie poziome\n-1 - odbicie względem obu osi\n"))

    if wybor == 0:
        obraz_po_odbiciu = cv2.flip(obraz, 0)
    elif wybor == 1:
        obraz_po_odbiciu = cv2.flip(obraz, 1)
    elif wybor == -1:
        obraz_po_odbiciu = cv2.flip(obraz, -1)
    else:
        print("Nieprawidłowy wybór!")
        exit()

    cv2.imshow('Obraz po odbiciu', obraz_po_odbiciu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
