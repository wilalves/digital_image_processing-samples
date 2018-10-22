import cv2

img1 = cv2.imread('images/image1.jpg')
img2 = cv2.imread('images/image2.jpg')


paste_image = cv2.add(img1, img2)

cv2.imshow('paste image', paste_image)
cv2.waitKey(0)
