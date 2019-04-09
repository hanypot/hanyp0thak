from random import randint as rand # importujem randint na generovanie náhodného čísla
from tkinter import * # ui
import os # magic
import sys # magic
import socket # magic

window = Tk()
window.title("HanyPot xd")
window.geometry('250x100')



lbl = Label(window, text = "u gay m8")
lbl.grid(row = 0, column = 0)



text = StringVar()
cmd_let = Entry(window, textvariable = text)
cmd_let.grid(row=3, column=5)


def clicked():
	klik = Label(window, text = "klik m8")
	klik.grid(row = 2, column = 0)
	os.system(text.get())

btn = Button(window, text = "Init", command = clicked)
btn.grid(row = 5, column = 0)

window.mainloop()
