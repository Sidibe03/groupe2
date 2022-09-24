

#page acceuil magasinier
from subprocess import call
from tkinter import *
from tkinter import ttk
#import mysql.connector
from tkinter import messagebox

def prodmag():
    fenetre2.destroy()
    call(["python","prodmag.py"])
def acceuil():
    fenetre2.destroy()
    call(["python","acceuilmag.py"])
def statiquemag():
    fenetre2.destroy()
    call(["python","statiquemag.py"])
def fournmag():
    fenetre2.destroy()
    call(["python","fourmag.py"])
def fenetre():
    fenetre2.destroy()
    call(["python","acceilmag.py"])
def livrmag():
    fenetre2.destroy()
    call(["python","livrmag.py"])




fenetre2 = Tk()
fenetre2.title("page d'acceil Magasinier")
fenetre2.geometry("1000x620")
fenetre2.resizable(False, False)
fenetre2.configure(bg="white")

# menu
menu = Frame(fenetre2, background="#395fb8", width="250", height="425")
menu.place(x=745, y=190)


label = Label(menu, text="Menu", font=("Arial_bold", 30), bg='#395FB8', fg='white')
label.place(x='30', y='')
bouton = Button(menu, text="Acceil", font=("", 20), width=13,command=acceuil)
bouton.place(x='10', y='60')
bouton = Button(menu, text="Produits", font=("", 20), width=13,command=prodmag)
bouton.place(x='10', y='140')
bouton = Button(menu, text="Statistiques", font=("", 20),width=13,command=statiquemag)
bouton.place(x='10', y='220')
bouton = Button(menu, text="Fournisseurs", font=("", 20),width=13,command=fournmag)
bouton.place(x='10', y='300')
bouton = Button(menu, text="Deconnexion", font=("", 20), bg='#060638', fg='white',command=fenetre)
bouton.place(x='25', y='360')
# acceuil
acc = Frame(fenetre2, background="#d9d9d9", width="1000", height="185")
acc.place(x="", y="")
    # logo
logo = Label(acc, text="BIG",bg="#d9d9d9",font=('Italic',35))
logo.place(x="95", y="40")
logo = Label(acc, text="STOCK", bg="#d9d9d9", font=('Italic', 35))
logo.place(x="57", y="95")
    #recherche
logo = Label(acc, text="Recherche", bg="white", font=('Italic', 15))
logo.place(x="500", y="120")
    # logo=PhotoImage(file=r"BIG STOCK1.png")
    # img=Button( image=logo).place(x=10,y=20)


# corps
acc = Frame(fenetre2, background="#d9d9d9", width="740", height="425")
acc.place(x="", y="190")

prod = Button(acc, text="Produits", bg="#395fb8",command=prodmag, fg="white", font=('', 25,), width="15", height="3")
prod.place(x="35", y="20")
prod = Button(acc, text="Livraisons", bg="#395fb8",command=livrmag, fg="white", font=('', 25,), width="15", height="3")
prod.place(x="400", y="20")

prod = Button(acc, text="Fournisseurs", bg="#395fb8", fg="white",command=fournmag, font=('', 25,), width="15", height="3")
prod.place(x="35", y="200")
prod = Button(acc, text="Statistique", bg="#395fb8", fg="white",command=statiquemag, font=('', 25,), width="15", height="3")
prod.place(x="400", y="200")

# copyrith
preven = Label(acc, text="Copyright @ 0101 par Groupe 2/ODC")
preven.place(x="250", y="400")

fenetre2.mainloop()
