import socket 

hedef_sunucu = "www.facebook.com"
hedef_port = 443

sunucu = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

sunucu.connect((hedef_sunucu , hedef_port))

sunucu.send("GET / HTTP/1.1\r\nHost: facebook.com\r\n\r\n")

response = sunucu.recv(4096)

print(response)

