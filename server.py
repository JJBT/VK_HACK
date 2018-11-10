import socket
import pickle
from PIL import Image
import os
import cv2
from keras.preprocessing.image import ImageDataGenerator, \
    img_to_array, load_img

from Constants import *


sock = socket.socket()
sock.bind(('', TCP_PORT))
sock.listen(True)

conn, addr = sock.accept()

print('connected:', addr)

while True:

    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 123)
    recognizer.read('recognizer.xml')

    data = conn.recv(1024)

    if not data:
        break

    # print('user - ', addr, ' send - ', data)
    conn.send(data.upper())

conn.close()
