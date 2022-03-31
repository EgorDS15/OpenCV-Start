import cv2 as cv


# img = cv.imread("Data\\woman.jpg")

# Enter path to your video file
vid = cv.VideoCapture('')


def res_im(frame, scale=.7):
    """ Images, Videos and Live Video """
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w, h)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def change_vid_res(width, height):
    """ Only for Live Video """
    vid.set(3, width)
    vid.set(4, height)


while True:
    isTrue, frame = vid.read()

    resized_frame = res_im(frame)

    cv.imshow('We are', frame)
    cv.imshow('We are res', resized_frame)

    if cv.waitKey(0) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
