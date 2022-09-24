

#page produit magasinier
from subprocess import call
from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox
#page produit magasinier


def prodmag():
    fenetre5.destroy()
    call(["python","prodmag.py"])
def acceuil():
    fenetre5.destroy()
    call(["python","acceuilmag.py"])
def statiquemag():
    fenetre5.destroy()
    call(["python","statiquemag.py"])
def fournmag():
    fenetre5.destroy()
    call(["python","fourmag.py"])
def fenetre():
    fenetre5.destroy()
    call(["python","acceilmag.py"])
def livrmag():
    fenetre5.destroy()
    call(["python","livremag.py"])
def modifprod():
    fenetre5.destroy()
    call(["python","modifprod.py"])


fenetre5=Tk()
fenetre5.title("produits Magasiniier")
fenetre5.geometry("1000x620")
fenetre5.resizable(False, False)
fenetre5.configure(bg="white")

    # menu
menu = Frame(fenetre5, background="#395fb8", width="250", height="425")
menu.place(x=745, y=190)

label = Label(menu, text="Menu", font=("Arial_bold", 30), bg='#395FB8', fg='white')
label.place(x='30', y='')
bouton = Button(menu, text="Acceil", font=("", 20), width=13, command=acceuil)
bouton.place(x='10', y='60')
bouton = Button(menu, text="Produits", font=("", 20), width=13, command=prodmag)
bouton.place(x='10', y='140')
bouton = Button(menu, text="Statistiques", font=("", 20), width=13, command=statiquemag)
bouton.place(x='10', y='220')
bouton = Button(menu, text="Fournisseurs", font=("", 20), width=13, command=fournmag)
bouton.place(x='10', y='300')
bouton = Button(menu, text="Deconnexion", font=("", 20), bg='#060638', fg='white', command=fenetre)
bouton.place(x='25', y='360')
    # acceuil
acc = Frame(fenetre5, background="#d9d9d9", width="1000", height="185")
acc.place(x="", y="")

    # corps
acc = Frame(fenetre5, background="#d9d9d9", width="740", height="425")
acc.place(x="", y=190)

text=Label(acc,text="Les Produits",font=('Italic',30),bg="#d9d9d9")
text.place(x=280, y=20)
    #affichage
columns = ('first_name', 'last_name', 'email','date')

tree = ttk.Treeview(acc, columns=columns, show='headings')
tree.place(x="",y=80)

    # define headings
tree.heading('first_name', text='ID')
tree.heading('last_name', text='NOM')
tree.heading('email', text='QUANTITE')
tree.heading('date', text='DATE ARRIVEE')

    # les butons

ajout = Button(acc, text="Ajouter", bg="#082EF5", fg="white", command=modifprod)
ajout.place(x="550", y="350")
supp = Button(acc, text="Supprimer", bg="#082EF5", fg="white", command=modifprod)
supp.place(x=650, y=350)
    # copyrith
preven = Label(acc, text="Copyright @ 0101 par Groupe 2/ODC")
preven.place(x=250, y=400)


fenetre5.mainloop()