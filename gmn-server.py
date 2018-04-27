#!/env/python
import socket

file = "mmcblk0"
port = 1337

def device_get_sector_size(device):
	with open("/sys/block/{0}/queue/physical_block_size".format(device)) as dev:
		return int(dev.read())
		
def device_get_sector_count(device):
	with open("/sys/block/{0}/size".format(device)) as dev:
		return int(dev.read())
		
def device_get_size(device):
	return device_get_sector_count(device) * device_get_sector_size(device)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), port))
sock.listen(1)

(client_socket, client_ip) = sock.accept()

sent = 0
total = device_get_size(file)

with open("/dev/block/{0}".format(file), "rb") as block:
	while(sent < total):
		block.seek(sent)
		data = block.read(4096)
		sent += client_socket.send(data)
		print(str(sent) + ' of ' + str(total))


