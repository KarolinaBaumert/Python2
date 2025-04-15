import cv2

image = cv2.imread('image.jpg')
if image is None:
    print("Nie znaleziono obrazu!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

def update(x):
    try:
        block_size = cv2.getTrackbarPos('BlockSize', 'Segmentacja')
        c_value = cv2.getTrackbarPos('C', 'Segmentacja') - 20
    except:
        return

    if block_size % 2 == 0:
        block_size += 1
    if block_size < 3:
        block_size = 3

    thresh = cv2.adaptiveThreshold(blurred, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV,
                                   block_size,
                                   c_value)

    cv2.imshow('Segmentacja', thresh)

cv2.namedWindow('Segmentacja')

cv2.createTrackbar('BlockSize', 'Segmentacja', 11, 51, update)
cv2.createTrackbar('C', 'Segmentacja', 20, 40, update)

update(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
