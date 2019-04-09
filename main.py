from random import randint as rand # importujem randint na generovanie náhodného čísla
from tkinter import * # ui
import os # magic
import sys # magic
import socket # magic
"""
TODO
-zisti ake slabiny ma vargov hanypot
- xd                                                -DONE
"""
window = Tk() # vytváram okno
window.title("xd") # nadpis na okne
window.geometry('200x200') # výška a šírka okna

def clicked():
	clickedtxt = Label(window, text = "done") # xd
	clickedtxt.grid(row = 7, column = 6)
	os.system(text.get())


btn = Button(window, text = "Init", command = clicked)
btn.grid(row = 0, column = 10)


text = StringVar()
cmd_let = Entry(window, textvariable = text) # text field
cmd_let.grid(row=10, column=0)




window.mainloop()
