import cv2 as cv
import numpy as np


img = cv.imread("Data\\woman.jpg")
# cv.imshow('photo', img)

# Edge cascade, low values - more details
canny = cv.Canny(img, 120, 120)
# cv.imshow('blank', canny)

# Borders in Gray are more clearly
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny1 = cv.Canny(gray, 120, 120)
# cv.imshow('blank1', canny1)
# canny1 = cv.Canny(img, 50, 75)
# canny2 = cv.Canny(img, 250, 50)
# canny3 = cv.Canny(img, 50, 275)
# cv.imshow('blank1', canny1)
# cv.imshow('blank2', canny2)
# cv.imshow('blank3', canny3)

# Dilating the image. Increase borders on image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow('blank1', dilated)

# dilated1 = cv.dilate(img, (13, 13), iterations=13)
# cv.imshow('blank2', dilated1)

# Reverse dilating operation
erode = cv.erode(dilated, (7, 7), iterations=3)
# cv.imshow('blank', erode)

"""
TAKES ONLY CANNY(EDGE) IMAGE 
Contours modes:
    RETR_TREE - hierarchial contours
    RETR_LIST - all contours
    RETR_EXTERNAL - external contours

cv.CHAIN_APPROX_NONE - aprox method

contours - list of all contours coordinates
hierarchies - hierarchies of contours 
"""
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Count of contours
print(len(contours))  # 146

# But if we blur image...
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# Then find edges...
canny2 = cv.Canny(blur, 120, 120)
# And count...
contours1, hierarchies = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Count of contours
print(len(contours1))  # 57!!! Number of contours was decreased
# cv.imshow('s', canny)
# cv.imshow('s1', canny2)

# Threshold image
ret, thresh = cv.threshold(img, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

canny3 = cv.Canny(thresh, 120, 120)
# cv.imshow('thresh1', canny3)


# How to draw on blank by any color
blank = np.zeros(img.shape, 'uint8')  # create blank with image size
contours2, hierarchies = cv.findContours(canny3, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # Find coordinates of edges
cv.drawContours(blank, contours2, -1, (255, 0, 0), 1)  # Draw
# cv.imshow('Drawn Contours', blank)  # See

"""
So:
1. cv.Canny()
2. cv.threshold()
3. cv.findContours()
Maybe great effect of edge detection will be with Blur!!!
"""

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.abs(lap))
# cv.imshow('lap', lap)

sobel_y = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_x = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)

# bitwise OR. Combine
combine = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('combine', combine)

cv.waitKey(0)
cv.destroyAllWindows()
