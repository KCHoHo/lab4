# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
count = 0
while count < 10:
    x = {"name": "Hao", "age":10+count, "city":"Ottawa"}
    data = json.dumps(x)
    print(data)
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    count +=1

#s.shutdown(1)
