import socket

host = "localhost"
port = 12345
address = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)

print(f"Server is waiting for connection at {host}:{port}")

connected = True
while connected:
  client, addr = s.accept()
  print(f"received connection request from client {addr}")
  msg = client.recv(1024).decode()
  print(f"received {msg}")
  client.sendall("Hello from server".encode())
  if msg == "stop":
    connected = False

s.close()