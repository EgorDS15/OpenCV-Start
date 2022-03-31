import numpy as np
import cv2 as cv

img = cv.imread("Data\\woman.jpg")
# cv.imshow('img', img)

blank = np.zeros(img.shape[:2], 'uint8')
# cv.imshow('blank', blank)

# create a circle. In shape tuples - first as X, second as Y. Changing values we change placement of figure
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('circle', circle)

# Bitwise AND
bit_and = cv.bitwise_and(img, img, mask=circle)
# cv.imshow('bit_and', bit_and)

# Bitwise OR
bit_or = cv.bitwise_or(img, img, mask=circle)
cv.imshow('bit_or', bit_or)

# Bitwise XOR
bit_xor = cv.bitwise_xor(img, img, mask=circle)
cv.imshow('bit_xor', bit_xor)


while True:
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cv.destroyAllWindows()
