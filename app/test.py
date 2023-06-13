# Test the model who was trained on: https://teachablemachine.withgoogle.com/train/image

import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0) # Open a video capture
detector = HandDetector(maxHands=1) # define max hands on the screen and calling the HandDetector function
classifier = Classifier("../../IaSignLanguageProject/Model/keras_model.h5", "../../IaSignLanguageProject/Model/labels.txt") # Function to classificate 


offset = 20
imgSize = 300

folder = "../../IaSignLanguageProject/Data/TOMARNO"
counter = 0

labels = ["A","B","C","D","E","F","G"]

while True:
    sucess, img = cap.read() # Reading the capture and put on img variable
    imgOutput = img.copy()  #remove the hand draw. If you want to put the hand draw, remove this variable and use just the img variable
    hands, img = detector.findHands(img) # Put the HandDetector function into the video capture (cap)
    if hands:   # if have some hand, the program will crop the image and open a new window with just the hand
        hand = hands[0]
        x,y,w,h = hand['bbox'] # x = horizoltal; y = vertical; w = width; h = height
        
        if w > 0 and h > 0: # Check if width and height are positive
            imgCrop = imgOutput[y-offset:y + h+offset, x-offset:x + w+offset]

            if imgCrop.size > 0:    # Check if imgCrop is not empty
                imgCrop = cv2.resize(imgCrop, (imgSize, imgSize))  # Resize imgCrop to match imgWhite shape

                imgWhite = np.ones((imgSize,imgSize, 3),np.uint8)*255 # creating a matrix and putting a fix size on the image

                imgCropShape = imgCrop.shape
                

                aspectRatio = h/w

                if aspectRatio > 1:
                    k = imgSize/h
                    wCal = math.ceil(k*w)
                    imgResize = cv2.resize(imgCrop,(wCal,imgSize))
                    imgResizeShape = imgResize.shape
                    wGap = math.ceil((imgSize-wCal)/2)
                    imgWhite[:,wGap:wCal+wGap] = imgResize # Define a fix size to the imagehand
                    prediction, index = classifier.getPrediction(imgWhite,draw=False)
                    print(prediction, index)
                
                else:
                    k = imgSize/w
                    hCal = math.ceil(k*h)
                    imgResize = cv2.resize(imgCrop,(imgSize,hCal))
                    imgResizeShape = imgResize.shape
                    hGap = math.ceil((imgSize-hCal)/2)
                    imgWhite[hGap:hCal+hGap,:] = imgResize # Define a fix size to the imagehand
                    prediction, index = classifier.getPrediction(imgWhite,draw=False)
                
                cv2.putText(imgOutput, labels[index],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
                cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,0,255),4)

                cv2.imshow("ImageCrop", imgCrop)
                cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", imgOutput) # To ajust the image from your original size
    cv2.waitKey(1) # allows users to display a window for given milliseconds or until any key is pressed
