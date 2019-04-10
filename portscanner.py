from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 0
min_port = 5000

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

try:
	host = input("[*] Target host address: ")
except KeyboardInterrupt:
	print("\n\n[-] User requested an interrupt")
	sys.exit(1)

hostip = gethostbyname(host)
print("\n[*] Host %s IP: %s" % (host, hostip))
print("[*] Scanning Started at %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
	try:
		response = scan_host(host, port)

		if response == 0:
			print("[*] Port %d: Open" % (port))
	except Exception:
		pass

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scanning finished at: %s...\n" % (time.strftime("%H:%M:%S")))
print("[*] Scanning duration: %s ..." % (total_time_duration))