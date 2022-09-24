


#page de connexion
from subprocess import call
from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox


def prodmag():
    fenetre1.destroy()
    call(["python","prodmag.py"])
def acceuil():
    fenetre1.destroy()
    call(["python","acceuilmag.py"])
def statiquemag():
    fenetre1.destroy()
    call(["python","statiquemag.py"])
def fournmag():
    fenetre1.destroy()
    call(["python","fourmag.py"])
def fenetre():
    fenetre1.destroy()
    call(["python","acceilmag.py"])
def livrmag():
    fenetre1.destroy()
    call(["python","livremag.py"])
def creation():
    fenetre1.destroy()
    call(["python","ceationcompte.py"])




    #fenetre pricipale
fenetre1=Tk()
fenetre1.geometry("1000x620")
fenetre1.resizable(False, False)
fenetre1.configure(bg="white")
fenetre1.title("page de connexion")

    #cadre pricipale
cadre=Frame(fenetre1,bg="#d9d9d9",width=500,height=350)

texte=Label (cadre,text="BigStock",font=('Italic',25),bg="#d9d9d9")
texte.place(x=190,y=40,)


texte=Label (cadre,text="Email",font=('Italic',12),bg="#d9d9d9")
texte.place(x=100,y=140)
champ=Entry(cadre,bg="#b1b8c8",width=30)
champ.place(x=200,y=140,)

texte=Label (cadre,text="password",font=('Italic',12),bg="#d9d9d9")
texte.place(x=100,y=180)
champ=Entry(cadre,bg="#b1b8c8",width=30)
champ.place(x=200,y=180,)

but=Button(cadre,bg="#b1b8c8",text="Connexion",command=acceuil)
but.place(x=210,y=260,)


pad=Button(cadre,text="Pas de compte",command=creation,bg="#d9d9d9")
pad.place(x=200,y=300,)

cadre.place(relx=0.5, rely=0.5, anchor=CENTER)
    #cadre.pack(padx=20, pady=20)

fenetre1.mainloop()


# if __name__ == '__main__':
#     fenetre()

