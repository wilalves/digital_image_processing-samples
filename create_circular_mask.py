import numpy as np
import cv2

def createCircularMask(h, w, center=None, radius=None):

    if center is None:
        center = [int(w/2), int(h/2)]
    if radius is None:
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask


if __name__ == '__main__':
    img = cv2.imread("images/amigos.jpg")
    cv2.imshow("original image", img)

    h, w = img.shape[:2]
    radius = h / 6
    # mask = createCircularMask(h, w, radius=radius)
    mask = createCircularMask(h, w)
    masked_img = img.copy()
    masked_img[~mask] = 0

    cv2.imshow("masked image", masked_img)
    cv2.waitKey(0)
