from random import randint as rand # importujem randint na generovanie náhodného čísla
from tkinter import * # ui
import os # magic
import sys # magic
import socket # magic
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

window.mainloop()