import cv2
import numpy as np
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import io
import os

from google.cloud import vision
from google.cloud.vision import types


# face_cascades = cv2.CascadeClassifier('cascade_frontal_face_default.xml')

client = vision.ImageAnnotatorClient()

file_name = 'C:/Users/Vladimyr/Desktop/photo_test_image.jpg'

with open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels')
for label in labels:
    print(label.description)
