import numpy as np
import cv2
import os
from PIL import Image

def pipeline_image_recognizer(image_path):
    person_label_predicted = -1
    labels_to_names = {-1: 'unknown', 0: 'chaikovsky', 1: 'rahmaninov', 2: 'shostakovich'}
    
    image = np.array(Image.open(image_path).convert('L'), 'uint8')
    face = face_cascades.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x_margin, y_margin, face_width, face_height) in face:
        person_label_predicted, = \
            recognizer.predict(image[y_margin: y_margin + face_height, x_margin: x_margin + face_width])
    return person_label_predicted, labels_to_names[person_label_predicted]
