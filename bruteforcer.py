from socket import *
import sys, time
from datetime import datetime

host = '192.168.100.62'

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		code = s.connect_ex((host, port))

		if code == 0:
			r_code = code
		s.close
	except Exception:
		pass
	return(r_code)


hostip = gethostbyname(host)


try:
	response = scan_host(host, port)

	if response == 0:
		isopen = True
except Exception:
		pass

