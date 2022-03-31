import cv2


frame_w = 640
frame_h = 480

# Class for video capturing from video files, image sequences or cameras.
cap = cv2.VideoCapture(0)

# we can see some parameters by using .get() method
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# And we can set parameters values by using .set() method
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
print(ret)

# Sometimes, cap may not have initialized the capture. In that case, this code shows an error. You can check whether
# it is initialized or not by the method cap.isOpened(). If it is True, OK. Otherwise open it using cap.open().
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # returns a bool (True/False)
    success, img = cap.read()

    # Our operations on the frame come here. We create new edited object with - img. gray - is object with new colors
    # parameters
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # we can comment previous line and uncomment line below to see camera capture without any changes
    # img = cv2.imshow('Video', img)

    # Display the resulting frame. If we use commented img at previous lines we should change gray to img in .imshow()
    # parameters
    cv2.imshow('img', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
