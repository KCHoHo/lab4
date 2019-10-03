# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
count = 0


while count < 10:
    count += 1
    data = random.randint(0,10)
#    s.sendall(data.encode('utf-8'))
    s.sendto(str(data).encode('utf-8'), server_address)

#s.shutdown(1)