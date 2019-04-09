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
	os.system(text.get())

btn = Button(window, text = "Init", command = clicked)
btn.grid(row = 20, column = 0)

text = StringVar()
cmd_let = Entry(window, textvariable = text) # text field
cmd_let.grid(row=10, column=0)

def send(msg): # function for sending the messages with the message text as a parameter
    client_socket.send(bytes(msg, "utf8")) #send the message to the server


HOST = None #vargov hanypot ip
PORT = None #vargov hanypot port
BUFSIZ = 1024
ADDR = (HOST, PORT) # adresa xd

client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(ADDR)

window.mainloop()