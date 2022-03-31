import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object. we should specify the FourCC code. MJPG (.mp4), DIVX (.avi),
# X264 (.mkv).
fourcc = cv.VideoWriter_fourcc(*'DIVX')

# We should specify the output file name (eg: output.avi). Then number of frames per second (fps) and
# # frame size should be passed.
# Enter path to your video file
out = cv.VideoWriter('\\output.avi', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # flip video
    frame = cv.flip(frame, 0)

    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
