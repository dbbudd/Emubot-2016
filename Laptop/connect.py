import socket
HOST, PORT = "192.168.100.1", 9999
data = "some_nans"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("connect ready")
