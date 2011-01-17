import socket
import time

host = 'localhost' 
port = 50000
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while True: 
    client, address = s.accept()
    data = client.recv(size)
    if data: 
        # assume data is line of text with two floats separated by spaces
        x, y = [ float(n) for n in data.split(' ')]
        client.send(str(x+y))  
    client.close()


