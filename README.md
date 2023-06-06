# Sign Language Ia

## Code Instalation

- Open the terminal
- Paste "git clone https://github.com/pabloncf/SignLanguageIA.git" and press enter

## Libraries instalation

- Open the terminal
- Install this libraries with pip:
    * pip install tensorflow
    * pip install opencv-python
    * pip install mediapipe
    * pip install cvzone
    * pip install cv2

You can run the requirements.txt too, using: pip install -r requirements.txt

## Observation

- On /app/test.py, you have to change the model directory on code:
```
classifier = Classifier("C:/Users/Pablo/Documents/SignLanguageIa/Model/keras_model.h5", "C:/Users/Pablo/Documents/SignLanguageIa/Model/labels.txt") # Function to classificate 
```