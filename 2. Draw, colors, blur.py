import numpy as np
import cv2 as cv

img = cv.imread("Data\\woman.jpg")
# cv.imshow('photo', img)

# Create a black image. Shape and amount of channels. We will use RGB - 3
blank = np.zeros(img.shape[:2], dtype='uint8')
# blank = np.zeros((img.shape[0], img.shape[1], 3))


# change Color to Blue. Remember in openCV - BGR, not RGB
img[:] = 255, 0, 0
# cv.imshow('blank', img)

# To draw some basic figure in window we address to pixels in indexes
img[200:250, 150:200] = 0, 0, 255
# cv.imshow('blank', img)

# we can use numpy
slice_ = img[:, :, 0]

# If we want to set all the red pixels to zero - you do not need to split the channels first. Numpy indexing is faster:
# img[:, :, 2] = 0

'''
Splitting and Merging Image Channels
Sometimes you will need to work separately on the B,G,R channels of an image. In this case, you need to split the BGR
image into single channels.
'''
img = cv.imread("Data\\woman.jpg")

b, g, r = cv.split(img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)


# Also, we can see more understandable images
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# cv.imshow('b', blue)
# cv.imshow('g', green)
# cv.imshow('r', red)

'''
cv.split() is a costly operation (in terms of time). So use it only if necessary. Otherwise go for Numpy indexing.
'''

# In other cases, you may need to join these individual channels to create a BGR image. You can do this simply by:
img = cv.merge((b, g, r))

# Much easier convert BGR to RGB is:
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

'''
To draw a line, you need to pass starting and ending coordinates of line. We will create a black image and draw
a blue line on it from top-left to bottom-right corners.
'''
# Draw a diagonal blue line with thickness of 5 px
cap = cv.line(blank, (0, 0), (511, 511), (255, 0, 0), 5)

'''
To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. This time we will draw a
green rectangle at the top-right corner of image. (0, 0) - start pixels, (250, 250) - end rectangle pixels. Further
'''
# color and thickness
# cap = cv.rectangle(img, (0, 0), (250, 250), (0, 255, 0), 3)

# we can fill area of rectangle by using cv.FILLED in thickness parameter
rectangle = cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), cv.FILLED)
# cv.imshow('rectangle', rectangle)

# Filled figure by using -1 in thickness parameter
circle = cv.circle(blank, (447, 63), 63, (0, 0, 255), -1)
ellipse = cv.ellipse(blank, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
polylines = cv.polylines(blank, [pts], True, (0, 255, 255))


'''
Adding Text to Images
To put texts in images, you need specify following things.
    - Text data that you want to write
    - Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
    - Font type (Check cv.putText() docs for supported fonts)
    - Font Scale (specifies the size of font)regular things like color, thickness, lineType etc. For better look,
lineType = cv.LINE_AA is recommended.
'''
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(blank, 'Im fucking awesome', (10, 500), font, 1, (255, 255, 255), 2, cv.LINE_AA)

# cv.imshow("Display window", img)

# Change the color
# gray = cv.cvtColor(img, cv.COLORMAP_JET)
gray = cv.cvtColor(img, cv.COLORMAP_SPRING)
# cv.imshow('gray', gray)

# Blur. (5, 5) - blur kernel size, take only odd values
blur = cv.GaussianBlur(img, (9, 9), 0, cv.BORDER_DEFAULT)
# cv.imshow('GaussianBlur', blur)

# Averaging blur
avg = cv.blur(img, (9, 9))
# cv.imshow('avg', avg)

# Median blur
med = cv.blur(img, (9, 9))
# cv.imshow('med', med)

# blur in need place on image
bilateral = cv.bilateralFilter(img, 5, 15, 15)
# cv.imshow('bilateral', bilateral)

# Threshold image
ret, thresh = cv.threshold(img, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# Threshold image
ret1, thresh1 = cv.threshold(img, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh1', thresh1)

# Adaptive Thresholding
adptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adptive_thresh', adptive_thresh)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.imwrite("LOL.png", img)
        break

# When everything done, release the capture
cv.destroyAllWindows()
