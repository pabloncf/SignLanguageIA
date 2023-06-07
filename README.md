# Configuration

## Code Instalation

- Open the terminal
- Paste "git clone https://github.com/pabloncf/SignLanguageIA.git" and press enter

## Libraries instalation

- Open the terminal
- Install these libraries with pip:
    * pip install tensorflow
    * pip install opencv-python
    * pip install mediapipe
    * pip install cvzone
    * pip install cv2

You can run the requirements.txt too, using: pip install -r requirements.txt

# How to use

## Data Collection

- in the file "dataCollection.py" you can make your own data base to train. To use, just run the code and make the hand positions, after that press "s" to save the pictures.

## Train the data

- To train, we used the website "https://teachablemachine.withgoogle.com/". *Just folow the website instructions and put your data*

## Use the aplication

- After train the data, you have to change the current model and put your model on /app/test.py:
```
classifier = Classifier("C:/Users/Pablo/Documents/SignLanguageIa/Model/keras_model.h5", "C:/Users/Pablo/Documents/SignLanguageIa/Model/labels.txt")
```



## Enjoy :)