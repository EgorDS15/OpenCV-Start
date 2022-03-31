import cv2 as cv
import os
import numpy as np

# Find folders names as people names
people = []
data_path = 'Data\\Recognizing'
for i in os.listdir(data_path):
    people.append(i)

print(people)

# Create object of cascade pretrained model
haar_cascade = cv.CascadeClassifier('face_det.xml')

features = []
labels = []


def create_train():
    # Iterate all persons
    for i in people:
        # find path of each person
        # path = data_path + '\\' + i
        path = os.path.join(data_path, i)
        label = people.index(i)

        # find path of each photo of person
        for j in os.listdir(path):
            img_path = os.path.join(path, j)

            # read img
            img = cv.imread(img_path)
            # convert to gray color
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in face_rect:
                # cropping face
                face_crop = img_gray[y:y+h, x:x+w]
                # append features and label of person
                features.append(face_crop)
                labels.append(label)
                # cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=3)


create_train()

# print(f'Num Faces - {len(features)}, Num Labels - {len(labels)}')

# Create recognizer
face_recog = cv.face.LBPHFaceRecognizer_create()

features = np.array(features, dtype='object')
labels = np.array(labels)

# Train model
face_recog.train(features, labels)

# Save numpy features, that allows to us dont repeat all code above
np.save('features.npy', features)
np.save('labels.npy', labels)

# We can save pretrained model by using yml-file.
face_recog.save('face_shaq-vince.yml')

# Let's continue in next script...
