# Image Addition
# You can add two images with the OpenCV function, cv.add(), or simply by the numpy operation res = img1 + img2. Both
# images should be of same depth and type, or the second image can just be a scalar value.
# There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a saturated operation while
# Numpy addition is a modulo operation.
import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])

print(x + y)
print(cv.add(x, y))

img1 = cv.imread("Data\\woman.jpg")
img2 = cv.imread("Data\\couple.jpeg")

# make second image same shape as img1. That is necessarily
img2 = img2[0:500, 0:500]

# dst = α ⋅ img1 + β ⋅ img2 + γ, where is alpha and beta is transparency coefficients
# dst = cv.addWeighted(img1, 0.5, img2, 0.5, 0)

# cv.imshow('dst', dst)


# Bitwise Operations
# This includes the bitwise AND, OR, NOT, and XOR operations. They will be highly useful while extracting any part of
# the image (as we will see in coming chapters), defining and working with non-rectangular ROI's, and etc. Below we
# will see an example of how to change a particular region of an image.
# I want to put the OpenCV logo above an image. If I add two images, it will change the color. If I blend them, I get a
# transparent effect. But I want it to be opaque. If it was a rectangular region, I could use ROI as we did in the last
# chapter. But the OpenCV logo is a not a rectangular shape. So you can do it with bitwise operations as shown below:
# So I create a ROI
rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]

# Now create a mask and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)


k = cv.waitKey(0)

cv.destroyAllWindows()
