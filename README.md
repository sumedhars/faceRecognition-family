# faceRecognition-family

This project is for the NVIDIA Jetson AI Specialist course.

The aim of this project is to recognize the faces of the people in my family. 
The situation that inspired me to do this project: Our house has a camera at the main door, that the people inside can use to see who is at the main door.
This software could be potentially used to help detect who is at the door, and if there was an unknown person, i.e. a non family member, the software would
detect the unknown person's face and label it as 'Unknown Person'.

Step/Details to run this project:
1. The 'train_family.pkl' file is a pickle file that stores the training data used to detect my family member's faces. To train this model from scratch,
the 'train_family.pkl' file can be deleted. To add more training data/faces to the model, add more face images to the familyImages directory. It is 
crucial that the file is named as 'FirstName LastName.jpg'. Only one image of the person is needed to train the model.
2. To train the model on my family member's faces, run the trainSave.py file. A 'train_family.pkl' file will be generated. 
3. To run the model using a webcam, run the faceRecognize-liveVideo.py file. The webcam will start up and will start recognizing faces.
4. To exit the application, press 'q' on your keyboard. Please note that pressing the 'x' on the pop-up window will simply restart a new camera window.


To make sure you have the necessary libraries to run the project, check out: https://www.youtube.com/watch?v=yOdVnQuhfeI
