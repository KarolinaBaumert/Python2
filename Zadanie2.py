import cv2
import numpy as np
import matplotlib.pyplot as plt

image_bgr = cv2.imread('image.jpg')
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

H, S, V = cv2.split(image_hsv)

S_mod = cv2.add(S, 30)

hsv_mod = cv2.merge([H, S_mod, V])

image_mod_rgb = cv2.cvtColor(hsv_mod, cv2.COLOR_HSV2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Oryginalny')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_mod_rgb)
plt.title('Zwiększone nasycenie (S +30)')
plt.axis('off')

plt.tight_layout()
plt.show()
