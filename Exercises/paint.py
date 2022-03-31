import cv2 as cv
import numpy as np


def nothing(x):
    pass


# mouse callback function
def draw_circle(event, x, y, flag, color):
    global ix, iy, drawing, mode, radius, e_shape
    # every condition is event and action for it
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x, y), radius, color, e_shape)
    elif event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), radius, color, e_shape)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img, (x, y), radius, color, e_shape)


# Attention! np.uint8 - is important parameter
img = np.zeros((340, 620, 3), np.uint8)

# true if mouse is pressed
drawing: bool = False

# if True, draw rectangle. Press 'm' to toggle to curve
mode = True
ix, iy = -1, -1

# Create name for future connections to window
cv.namedWindow('image')


# create trackbars for color change.  first argument is the trackbar name, second one is the window name to which
# it is attached, third argument is the default value, fourth one is the maximum value and fifth one is the callback
# function which is executed every time trackbar value changes. The callback function always has a default argument
# which is the trackbar position. In our case, 'function' does nothing, so we simply pass.
# Use it as a button or switch. OpenCV, by default, doesn't have button functionality.
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('Size', 'image', 0, 50, nothing)

# create switch for ON/OFF functionality
switch = '0-OFF\n1-ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)
cv.createTrackbar('Shape', 'image', -1, 10, nothing)

# Line thikness takes values between -1 and infinite. We need -1 for full shape, but for this we should set minimum
cv.setTrackbarMin('Shape', 'image', -1)


while True:
    cv.imshow('image', img)

    k = cv.waitKey(1)
    if k == ord('q'):
        break

    # enable for every Trackbar
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    radius = cv.getTrackbarPos('Size', 'image')
    e_shape = cv.getTrackbarPos('Shape', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    # If active condition then input channel for img is condition values from Trackbars, else is 0
    if s == 0:
        cv.setMouseCallback('image', draw_circle, [255, 255, 255])
    else:
        cv.setMouseCallback('image', draw_circle, [b, g, r])

cv.destroyAllWindows()
