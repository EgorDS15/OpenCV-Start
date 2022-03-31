import cv2 as cv

# Woman face
# img = cv.imread("Data\\woman.jpg")

# A pair of faces
img = cv.imread("Data\\couple.jpg")
# cv.imshow('woman', img)


# Color can input good and bad information about some objects in image. Right here we change color to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Turn on Face Classifier from .xml file
classifier = cv.CascadeClassifier('face_det.xml')

# Result. Higher values of minNeighbors is more noise
face = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# cv.imshow('face', face)
print('Number of faces {}'.format(len(face)))

# List with x, y, width and height of face
print(face)

# Draw rectangle over detected face
for (x, y, w, h) in face:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow('Face', img)


cv.waitKey(0)

cv.destroyAllWindows()