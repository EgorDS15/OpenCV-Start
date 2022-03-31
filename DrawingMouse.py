import cv2 as cv
import numpy as np

# How to see all events(actions what we can read from user)
from numpy import ndarray

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

# true if mouse is pressed
drawing = False

# if True, draw rectangle. Press 'm' to toggle to curve
mode = True
ix, iy = -1, -1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # every condition is event and action for it
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)

# Name of window
cv.namedWindow('double-click-circle')

# Name of created window and action function in this window
cv.setMouseCallback('double-click-circle', draw_circle)

while True:
    # see result
    cv.imshow('double-click-circle', img)
    # if we change the name in .imshow() we can see two windows - in first we act, in second see result
    # cv.imshow('one', img)
    k = cv.waitKey(20) & 0xFF
    # switch to one of the modes. By default - draw rectangle, when pressed once 'm' switch to circles
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break

cv.destroyAllWindows()

