# coding: utf-8

from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello You")
label.pack()

#label
label1 = Label(fenetre, text="Bonjour Dehbia", bg="green")
label1.pack()

#bouton de sortie 
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()