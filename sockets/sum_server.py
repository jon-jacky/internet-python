"""
Usage:

 python sum_server.py host port

for example:

 python localhost 50000

Omit trailing args to use defaults: localhost 50000
Client will exit with exception if args are wrong type or otherwise don't work
Client must send one string with two floats (as strings) separate by spaces
otherwise server will exit with exception.  sum_client only sends valid string.
"""

import socket
import sys

# defaults, override with command line args if present
host = 'localhost' 
port = 50000

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
print 'Listening on %s, port %s, with backlog %s, size %s' % \
    (host,port,backlog,size)
while True: 
    client, (local_host, port) = s.accept()
    print 'Accepting connection from %s, port %s' % (local_host, port)
    data = client.recv(size)
    if data: 
        # assume data is line of text with two floats separated by spaces
        print 'Received string: %s' % data
        x, y = [ float(n) for n in data.split(' ')]
        sum = str(x+y)
        print 'Send string    : %s' % sum
        client.send(sum)
    client.close()

