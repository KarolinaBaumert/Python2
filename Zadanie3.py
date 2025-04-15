import cv2

image = cv2.imread("kostka_brukowa1.jpg")
if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

block_size = 21
C_values = [2, 5, 10, 15]

for method, method_name in [(cv2.ADAPTIVE_THRESH_MEAN_C, "Mean"),
                            (cv2.ADAPTIVE_THRESH_GAUSSIAN_C, "Gaussian")]:
    for C in C_values:
        thresh = cv2.adaptiveThreshold(gray, 255,
                                       method,
                                       cv2.THRESH_BINARY,
                                       block_size, C)
        cv2.imshow(f"{method_name} - C={C}", thresh)

cv2.imshow("Oryginalny", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
