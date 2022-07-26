# code is inspired by video lessons on Paul McWhorter's Youtube page.

import face_recognition
import cv2
import os #lets us automate the training
import pickle
print(cv2.__version__)

Encodings = []
Names = [] 

image_dir = '/home/sumedha/faceRecognition-family/familyImages'
# walk your way through every file in 'known' directory. load the file, do the face encoding, get the name, fill in the encodings+names
for root, dirs, files in os.walk(image_dir): #starts in image directory, walk through all the files + directories + entire file structure
    #files -> an array of all of the files in image_dir
    for file in files:
        # create the actual complete path with the filename
        path = os.path.join(root, file) # path with the file
        name = os.path.splitext(file)[0] #removes the .jpg
        person = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(person)[0]
        Encodings.append(encoding)
        Names.append(name)

print(Names)

with open('train_family.pkl','wb') as f:
    pickle.dump(Names,f)
    pickle.dump(Encodings,f)