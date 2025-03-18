import cv2
import numpy as np

image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

diff = cv2.absdiff(image1, image2)

gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_diff, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Difference', diff)
cv2.imshow('Thresholded Difference', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
