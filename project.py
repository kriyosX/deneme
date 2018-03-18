import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ipv = input("=>")

ip = "ipv"
port = 80

s.connect(ip.port)
s.listen(ip.port)
print("Listening....")