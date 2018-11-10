import socket
import cv2
import numpy


from Constants import *


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(True)
conn, addr = s.accept()

data = 1

while True:
    length = recvall(conn, 16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')

    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 123)
    recognizer.read('recognizer.xml')

    # recognizer.predict()

s.close()

# decimg = cv2.imdecode(data, 1)
# cv2.imshow('SERVER',decimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
