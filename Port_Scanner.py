import socket 
import sys

ip="10.11.2.181"
port=80
print(ip)
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
result=server.connect_ex((ip,port))


print(result)
if result:
    print("port is open ")
else:
    print("port is not open ")