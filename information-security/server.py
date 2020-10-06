import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()   # get ip address of host
port = 444

serversocket.bind((host, port))

serversocket.listen(3) # 3 computers can connect only

while True:
    clientsocket, address = serversocket.accept()

    print('Received connection from ' % str(address))

    message = 'Helo! Thank you for connecting to the server' + '\r\n'

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()