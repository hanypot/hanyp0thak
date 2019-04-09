from random import randint as rand # importujem randint na generovanie náhodného čísla
from tkinter import * # ui
import os # magic
import sys # magic
import socket # magic
"""
TODO
-zisti ake slabiny ma vargov hanypot
-urob z tohoto este vacsi meme jak to je            -half-DONE
- xd                                                -DONE


"""
window = Tk() # vytváram okno
window.title("HanyPot xd") # nadpis na okne
window.geometry('250x100') # výška a šírka okna

def clicked():
	klik = Label(window, text = "klik m8") # xd
	klik.grid(row = 2, column = 0)
	bruh1 = Label(window, text = "bruh").grid(row = 6, column = 1)
	bruh2 = Label(window, )
	print("bruh wtf...")
	os.system(text.get())


btn = Button(window, text = "Init", command = clicked)
btn.grid(row = 5, column = 0)

lbl = Label(window, text = "u gay m8") # nápis U GAY M8
lbl.grid(row = 0, column = 0)


text = StringVar()
cmd_let = Entry(window, textvariable = text) # text field
cmd_let.grid(row=3, column=5)




window.mainloop()
