import numpy as np
import cv2


def createRectangularMask(img, x, y, w, h):

    mask = np.zeros(img.shape[:2], np.uint8)
    mask[y:y + h, x:x + w] = ~mask[y:y + h, x:x + w]
    mask = cv2.bitwise_and(img, img, mask=mask)

    return mask


if __name__ == '__main__':
    img = cv2.imread("images/amigos.jpg")
    cv2.imshow("original image", img)

    mask = createRectangularMask(img, 240, 130, 250, 300)
    masked_img = img.copy()
    masked_img[~mask] = 0

    cv2.imshow("masked image", masked_img)
    cv2.waitKey(0)
