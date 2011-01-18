"""
Usage:

 python sum_client.py host port x y

for example:

 python localhost 50000 1 2

Omit trailing args to use defaults: localhost 50000 0 0
Client will exit with exception if args are wrong type or otherwise don't work
x and y must be strings that convert to floats.
If this program succeeds, it sends string in valid form for sum_server
"""

import socket 
import sys

# defaults, override with command line args if present
host = 'localhost'
port = 50000 
x = 0
y = 0

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])
if nargs > 3:
    x = float(sys.argv[3]) # ValueError if arg doesn't convert to float
if nargs > 4:
    y = float(sys.argv[4])

size = 1024 
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
xy = '%s %s' % (str(x), str(y))
print 'Send numbers: %s' % xy
s.send(xy)
sum = s.recv(size) 
s.close() 
print 'Receive sum :', sum

