import socket
import threading

x_ip = "x.x.x.x"
x_port = 8080

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.x((x_ip , x_port))

s.listen(5)

print("Dinleniyor... %s %d" % (x_ip,x_port))

def handle_client-handling theread
    request = client_socket.recv(1024)

    print("[*] Tamamlandı: %s" & request)

    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr = s.accept()
    print("Bağlantı Kabul Edildi: %s %d" % (addr[0],aaddr[1]))

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()