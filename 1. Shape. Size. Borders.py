import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Data\\woman.jpg")
# cv.imshow('myPhoto', img)

'''
You can access a pixel value by its row and column coordinates. For BGR image, it returns an array of Blue, Green,
Red values. For grayscale image, just corresponding intensity is returned.
'''
print(img[100, 100])

# accessing only blue pixel
print(img[100, 100, 0])

'''
For individual pixel access, the Numpy array methods, array.item() and array.itemset() are considered better.
They always return a scalar, however, so if you want to access all the B,G,R values, you will need to
call array.item() separately for each value.
'''
print(img.item(15, 32, 2))

# shape
print(img.shape)

# image pixel amounts in 3 channels
print(img.size)

# dtype
print(img.dtype)

'''
Sometimes, you will have to play with certain regions of images. For eye detection in images, first face detection
is done over the entire image. When a face is obtained, we select the face region alone and search for eyes inside
it instead of searching the whole image. It improves accuracy (because eyes are always on faces :D ) and performance
(because we search in a small area).
'''
ball = img[200:300, 200:500]
img[100:200, 0:300] = ball

# cv.imshow('cropped', img)

# cv.imwrite("Cropped Image.jpg", ball)

'''
Making Borders for Images (Padding)
If you want to create a border around an image, something like a photo frame, you can use cv.copyMakeBorder().
But it has more applications for convolution operation, zero padding etc. This function takes following arguments:
PARAMETERS:
src - input image
top, bottom, left, right - border width in number of pixels in corresponding directions
borderType - Flag defining what kind of border to be added. It can be following types:
cv.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
cv.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this: fedcba|abcdefgh|hgfedcb
cv.BORDER_REFLECT_101 or cv.BORDER_DEFAULT - Same as above, but with a slight change, like this: gfedcb|abcdefgh|gfedcba
cv.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
cv.BORDER_WRAP - Can't explain, it will look like this : cdefgh|abcdefgh|abcdefg
value - Color of border if border type is cv.BORDER_CONSTANT
'''
# CV2 working with BGR, since PYPLOT working with RGB. So before plot we should split, change positions and merge
rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
BLUE = [255, 0, 0]

replicate = cv.copyMakeBorder(rgb_image, 60, 60, 60, 60, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(rgb_image, 60, 60, 60, 60, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(rgb_image, 60, 60, 60, 60, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(rgb_image, 60, 60, 60, 60, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(rgb_image, 60, 60, 60, 60, cv.BORDER_CONSTANT, value=BLUE)

plt.subplot(231)
plt.title('ORIGINAL')
plt.imshow(rgb_image)

plt.subplot(232)
plt.title('REPLICATE')
plt.imshow(replicate, 'gray')

plt.subplot(233)
plt.title('REFLECT')
plt.imshow(reflect, 'gray')

plt.subplot(234)
plt.title('REFLECT_101')
plt.imshow(reflect101, 'gray')

plt.subplot(235)
plt.title('WRAP')
plt.imshow(wrap, 'gray')

plt.subplot(236)
plt.title('CONSTANT')
plt.imshow(constant, 'gray')

plt.show()


# Resize
resized1 = cv.resize(img, (200, 300))
# cv.imshow('new1', resized1)
# resized2 = cv.resize(img, (200, 300), interpolation=cv.INTER_AREA)
# cv.imshow('new2', resized2)

'''
For increase image size use interpolations - INTER_LINEAR, INTER_CUBIC
'''
# resized3 = cv.resize(img, (700, 800), interpolation=cv.INTER_LINEAR)
# cv.imshow('new3', resized3)
# resized4 = cv.resize(img, (700, 800), interpolation=cv.INTER_CUBIC)
# cv.imshow('new4', resized4)

# Save image
# cv.imwrite("starry_night.png", img)


def res_im(frame, scale=.7):
    """ Images, Videos and Live Video """
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w, h)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def change_vid_res(video: cv.VideoCapture(), width, height):
    """ Only for Live Video """
    video.set(3, width)
    video.set(4, height)


k = cv.waitKey(0)

cv.destroyAllWindows()
