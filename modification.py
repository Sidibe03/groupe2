

#page de modification
from subprocess import call
from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox


def prodmag():
    modif.destroy()
    call(["python","prodmag.py"])
def acceuil():
    modif.destroy()
    call(["python","acceuilmag.py"])
def statiquemag():
    modif.destroy()
    call(["python","statiquemag.py"])
def fournmag():
    modif.destroy()
    call(["python","fourmag.py"])
def fenetre():
    modif.destroy()
    call(["python","acceilmag.py"])
def livrmag():
    modif.destroy()
    call(["python","livremag.py"])


modif = Tk()
modif.title("Modification")
modif.geometry("1000x620")
modif.resizable(False, False)
modif.configure(bg="white")

    # cadre pricipale
cadre = Frame(modif, bg="#d9d9d9", width=500, height=350)

texte = Label(cadre, text="Modification ", font=('Italic', 25), bg="#d9d9d9")
texte.place(x=160, y=40, )

texte = Label(cadre, text="Nom", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=10, y=140)
champ = Entry(cadre, bg="#b1b8c8", width=25)
champ.place(x=80, y=140, )

texte = Label(cadre, text="Prenom", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=250, y=140)
champ = Entry(cadre, bg="#b1b8c8", width=25)
champ.place(x=320, y=140, )

texte = Label(cadre, text="Telephone", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=10, y=180)
champ = Entry(cadre, bg="#b1b8c8", width=25)
champ.place(x=80, y=180, )

texte = Label(cadre, text="Email", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=250, y=180)
champ = Entry(cadre, bg="#b1b8c8", width=25)
champ.place(x=320, y=180, )

texte = Label(cadre, text="Date", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=10, y=220)
champ = Entry(cadre, bg="#b1b8c8", width=25)
champ.place(x=80, y=220, )


but = Button(cadre, bg="#b1b8c8", text="valider", command=quit)
but.place(x=210, y=260, )

cadre.place(relx=0.5, rely=0.5, anchor=CENTER)

modif.mainloop()
