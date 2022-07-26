# code is inspired by video lessons on Paul McWhorter's Youtube page.

import face_recognition
import cv2
import os
import pickle
print(cv2.__version__)

Encodings = [] # encoding for different faces that were trained on
Names = [] 
matches = []
name = ''

with open('train_family.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

font = cv2.FONT_HERSHEY_SIMPLEX

# launch camera
cam = cv2.VideoCapture(0)

while True:
    # grab the frame from the camera
    _,frame = cam.read()
    frameSmall = cv2.resize(frame,(0,0),fx=.20,fy=.20)
    frameRGB = cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)
    facePositions = face_recognition.face_locations(frameRGB,model='CNN')
    allEncodings = face_recognition.face_encodings(frameRGB,facePositions)
    #step through each found face and compare it to training data encodings
    for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
        name = 'Unknown Person'
        matches = face_recognition.compare_faces(Encodings,face_encoding)
        #face_encoding is the present unknown face in the frame that we just grabbed, and that is compared to encoding training data
        #matches will return an array of True and False, True when unknown matches one of the training
        if True in matches:
            first_match_index = matches.index(True)
            name = Names[first_match_index]
        top = top*5
        right = right*5
        bottom = bottom*5
        left = left*5
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,255),2)
        cv2.putText(frame,name,(left,top-6),font,.75,(255,0,0),2)

    cv2.imshow('Picture',frame)
    cv2.moveWindow('Picture',0,0)

    # exits application if you press q. opens new live camera if you press 'x' on window
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()