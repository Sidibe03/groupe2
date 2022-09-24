


#page modification produit
from subprocess import call
from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox
#page de modification produits


def prodmag():
    modifprod.destroy()
    call(["python","prodmag.py"])
def acceuil():
    modifprod.destroy()
    call(["python","acceuilmag.py"])
def statiquemag():
    modifprod.destroy()
    call(["python","statiquemag.py"])
def fournmag():
    modifprod.destroy()
    call(["python","fourmag.py"])
def fenetre():
    modifprod.destroy()
    call(["python","acceilmag.py"])
def livrmag():
    modifprod.destroy()
    call(["python","livremag.py"])

modifprod = Tk()
modifprod.title("Modifiacation des produits")
modifprod.geometry("1000x620")
modifprod.resizable(False, False)
modifprod.configure(bg="white")

    # ajouter fonction
    # def insert():
    #     id = champid.get();
    #     nom = champnom.get();
    #     quant = champquant.get();
    #     date = champdate.get();
    #
    #     con = mysql.connect(host="localhost", user="root", password="", database="bigstock")
    #     cursor = con.cursor()
    #     cursor.execute("insert into eleve values ('" + id + "','" + nom + "','" + quant + "','" + date + "') ")
    #     cursor.execute("commit");
    #
    #     con.close();

    # cadre pricipale
cadre = Frame(modifprod, bg="#d9d9d9", width=500, height=350)

texte = Label(cadre, text="Modification ", font=('Italic', 25), bg="#d9d9d9")
texte.place(x=160, y=40, )

texte = Label(cadre, text="Id", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=10, y=140)
champid = Entry(cadre, bg="#b1b8c8", width=25)
champid.place(x=60, y=140, )

texte = Label(cadre, text="Nom", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=10, y=180)
champnom = Entry(cadre, bg="#b1b8c8", width=25)
champnom.place(x=60, y=180 )

texte = Label(cadre, text="Quantité", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=240, y=140)
champid = Entry(cadre, bg="#b1b8c8", width=25)
champid.place(x=320, y=140, )

texte = Label(cadre, text="Date d'arrivée", font=('Italic', 10), bg="#d9d9d9")
texte.place(x=240, y=180)
champnom = Entry(cadre, bg="#b1b8c8", width=25)
champnom.place(x=320, y=180)



but = Button(cadre, bg="#b1b8c8", text="valider", command=quit)
but.place(x=210, y=260)

cadre.place(relx=0.5, rely=0.5, anchor=CENTER)

modifprod.mainloop()