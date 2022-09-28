

# page acceuil admin
from subprocess import call
from tkinter import *
from tkinter import ttk
import customtkinter as customtkinter
from PIL import Image, ImageTk


fenetre2 = Tk()
fenetre2.title("page d'acceil Admin")
fenetre2.geometry("1000x620")
fenetre2.resizable(False, False)
fenetre2.configure(bg="white")

def prodmag():
    fenetre2.destroy()
    call(["python", "produitadmin.py"])


def acceuil():
    fenetre2.destroy()
    call(["python", "accadmin.py"])

def forni():
    fenetre2.destroy()
    call(["python", "fournisseur.py"])



def mag():
    fenetre2.destroy()
    call(["python", "magasinier.py"])

def connexion():
    fenetre2.destroy()
    call(["python", "connexion.py"])



# corps
fram = Frame(fenetre2, bg='#FFFFFF', width='1000', height='250')
fram.place(x='', y='')

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\PycharmProjects\\bigstock\\fond1.png"))
x = Label(fram, image=photo)
x.place(x='', y='')

bouton = customtkinter.CTkButton(master=fram, text="Accueil", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=acceuil)
bouton.place(x='10', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Produits", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prodmag)
bouton.place(x='180', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Magasinier", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=mag)
bouton.place(x='360', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Fournisseur", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=forni)
bouton.place(x='570', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Deconnexion", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=connexion)
bouton.place(x='800', y='170')
# recherche
logo = Label(fram, text="Bienvenue Administrateur!!!", font=('Italic', 20))
logo.place(x="640", y="60")
# logo
logo = Label(fram, text=" BIGSTOCK", font=('Italic', 35))
logo.place(x="40", y="40")

fram0 = Frame(fenetre2, width='1000', height='370')
fram0.place(x='', y='250')


prod0 = Button(fram0, text="Total Produits\n      104", bg="#319BFE", command=quit(), fg="white", font=('', 25),
               width="15", height="3")
prod0.place(x="10", y="80")

prod1 = Button(fram0, text="Total Magasiniers\n     3", bg="#319BFE", command=quit(), fg="white", font=('', 25),
               width="15", height="3")
prod1.place(x="350", y="80")

prod2 = Button(fram0, text="Total Fournisseurs\n       15 ", bg="#319BFE", fg="white", command=quit(), font=('', 25),
               width="15", height="3")
prod2.place(x="700", y="80")

# copyrith
preven = Label(fenetre2, text="Copyright @ 0101 par Groupe 2/ODC", font=("Arial", 10))
preven.place(x="350", y="600")

fenetre2.mainloop()