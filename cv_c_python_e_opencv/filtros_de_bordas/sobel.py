import cv2
import matplotlib.pyplot as plt

img = cv2.imread("filtros_de_bordas/Imagens/predio.JPG")

sobelx = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=7)
sobely = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=7)

fig = plt.figure(figsize=(20, 50))

ax1 = fig.add_subplot(131)
plt.imshow(img)

ax2 = fig.add_subplot(132)
plt.imshow(sobelx)

ax3 = fig.add_subplot(133)
plt.imshow(sobely)

plt.show()
