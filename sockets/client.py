import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"Hello, world1")
data = s.recv(1024)
print(f"Received {data!r}")

s.sendall(b"Hello, world2")
data = s.recv(1024)
print(f"Received {data!r}")

s.close()
