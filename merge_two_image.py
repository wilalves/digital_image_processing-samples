import cv2


img1 = cv2.imread('images/image1.jpg')
img2 = cv2.imread('images/image2.jpg')

merge = cv2.addWeighted(img1, 0.5,img2,0.5,0)

cv2.imshow('merged images', merge)
cv2.waitKey(0)