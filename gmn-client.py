#!/env/python
import socket

ip = "localhost"
port = 1337
filename = "nand.bak"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

total = 0

with open(filename, "wb") as nand:
	nand.seek(0)
	while True:
		received = sock.recv(4096)
		if received == "" or len(received) == 0:
			break;
		total += len(received)
		print(total)
		nand.write(received)
	
	