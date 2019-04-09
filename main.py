from random import randint as rand # importujem randint na generovanie náhodného čísla
from tkinter import * # ui
import os # magic
import sys # magic
from socket import AF_INET, socket, SOCK_STREAM # magic
import time
"""
TODO
-zisti ake slabiny ma vargov hanypot
- xd                                                -DONE
"""
window = Tk() # vytváram okno
window.title("xd") # nadpis na okne
window.geometry('400x90') # výška a šírka okna

def clicked():
	#os.system(text.get())
	do = action.get()
	if do == "kras":
		client_socket.connect(ADDR)
		br = "a"
		send(br*BUFSIZ)
		print("oops")
	elif do == "mv":
		client_socket.connect(ADDR)
		# something
	elif do == "ch":
		client_socket.connect(ADDR)
		#something
	elif do == "showtime":
		print(":)")
		#something
	else:
		pass
		
btn = Button(window, text = "Init", command = clicked)
btn.grid(row = 20, column = 0)

action_chooser = Radiobutton(window, text = "Crash", value = "kras", variable = action)
action_chooser1 = Radiobutton(window, text = "Rename to -", value = "mv", variable = action)
action_chooser2 = Radiobutton(window, text = "Change password to -", value = "ch", variable = action)
action_chooser3 = Radiobutton(window, text = ":)", value = "showtime", variable = action)



text = StringVar()
cmd_let = Entry(window, textvariable = text) # text field
cmd_let.grid(row=10, column=0)

def send(msg):
    client_socket.send(bytes(msg, "utf8"))


HOST = None #vargov hanypot ip
PORT = None #vargov hanypot port
BUFSIZ = 1024
ADDR = (HOST, PORT) # adresa xd

client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(ADDR)
#br = "a"
#send(br*BUFSIZ)

window.mainloop()