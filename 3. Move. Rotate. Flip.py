import cv2 as cv
import numpy as np


img = cv.imread("Data\\woman.jpg")
cv.imshow('photo', img)


# Moving image
def move_img(image, x, y):
    """
    -x => Left
    -y => Up
    x => Right
    y => Down
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)


# moved_img = move_img(img, 100, -100)
# cv.imshow('windowName', moved_img)


# Rotation
def rotate(image, angle, rot_point=None):
    height, width = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rot_mat, dimensions)


# To rotate to another direction just enter negative value of angle. Also if we turn image for 45 and 45 again we'll
# see problems, so if we need rotate image for 45 degrees that was rotated earlier by 45(i. e example) at second time
# we just enter 90 degree.
rotated = rotate(img, 45)
# cv.imshow('rotated', rotated)


# Flipping
# flip = cv.flip(img, -1) # flip up and mirror
flip = cv.flip(img, 0)  # flip up
flip = cv.flip(img, 1)  # mirror
cv.imshow('fliped', flip)


cv.waitKey(0)
cv.destroyAllWindows()