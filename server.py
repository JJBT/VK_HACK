import socket

TCP_IP = ''
TCP_PORT = 5001

sock = socket.socket()
sock.bind(('', TCP_PORT))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    print('user - ', addr, ' send - ', data.decode())
    conn.send(data.upper())

conn.close()
