import socket

def scan(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		result = sock.connect_ex((host, port))
		if result == 0:
			return(True)
			sock.close()
		else:
			return(False)
			sock.close()
	except socket.error:
		pass
	except socket.gaierror:
		pass