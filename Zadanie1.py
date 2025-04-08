import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('redcar.jpg')  # zamień na nazwę swojego obrazu
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

R, G, B = cv2.split(image_rgb)

image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
H, S, V = cv2.split(image_hsv)

plt.figure(figsize=(12, 8))
plt.subplot(2, 4, 1)
plt.imshow(image_rgb)
plt.title("Oryginał RGB")
plt.axis('off')

plt.subplot(2, 4, 2)
plt.imshow(R, cmap='Reds')
plt.title("Kanał R")
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(G, cmap='Greens')
plt.title("Kanał G")
plt.axis('off')

plt.subplot(2, 4, 4)
plt.imshow(B, cmap='Blues')
plt.title("Kanał B")
plt.axis('off')

plt.subplot(2, 4, 5)
plt.imshow(cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB))
plt.title("Oryginał HSV")
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(H, cmap='hsv')
plt.title("Kanał H (Hue)")
plt.axis('off')

plt.subplot(2, 4, 7)
plt.imshow(S, cmap='gray')
plt.title("Kanał S (Saturation)")
plt.axis('off')

plt.subplot(2, 4, 8)
plt.imshow(V, cmap='gray')
plt.title("Kanał V (Value)")
plt.axis('off')

plt.tight_layout()
plt.show()
