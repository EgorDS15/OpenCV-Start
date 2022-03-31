import numpy as np
import cv2 as cv

all_labels = ['Carter', 'Shaq']

# load classifier to find the face
haar_cascade = cv.CascadeClassifier('face_det.xml')

# if we need import features for something
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

# load our pre-trained model to recognize the person
face_recog = cv.face.LBPHFaceRecognizer_create()
face_recog.read('face_shaq-vince.yml')

img = cv.imread('Data/Validation/fourth.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('pic', gray)

# Find the face on the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    # Predict
    label, confidence = face_recog.predict(faces_roi)
    print('This is {} with {} confidence.'.format(all_labels[label], confidence))

    cv.putText(img, str(all_labels[label]), (20, 20), cv.FONT_ITALIC, 1.0, (255, 0, 0), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

cv.imshow('Detected Face', img)

cv.waitKey(0)
