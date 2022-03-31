import numpy as np
import cv2 as cv


def nothing(x):
    pass


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)

cv.namedWindow('image')

# create trackbars for color change.  first argument is the trackbar name, second one is the window name to which
# it is attached, third argument is the default value, fourth one is the maximum value and fifth one is the callback
# function which is executed every time trackbar value changes. The callback function always has a default argument
# which is the trackbar position. In our case, 'function' does nothing, so we simply pass.
# Use it as a button or switch. OpenCV, by default, doesn't have button functionality.
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0-OFF\n1-ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
