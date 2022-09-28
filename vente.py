




from subprocess import call
from tkinter import *
from tkinter import ttk,Entry
import customtkinter
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


fenetre5=Tk()
fenetre5.title("Les ventes ")
fenetre5.geometry("1000x620")
fenetre5.resizable(False, False)
fenetre5.configure(bg="white")

# #fonction valider
# def valider():
#
#     con = mysql.connect(host="localhost", user="root", password="", database="bigstock")
#     cursor=con.cursor()
#     cursor.execute("select * from fournisseur ")
#     aff.delete(*aff.get_children())
#     records = cursor.fetchall()
#     print(records)
#
#     for i, (id,nom,prenom,tel,typro,adresse) in enumerate (records,start=1):
#             aff.insert ("", "end", values=(id,nom,prenom,tel,typro,adresse))
#     valider()
#     con.close()


texte=Label (fenetre5,text="Les Ventes",font=('Calistoga',25),bg="white")
texte.place(x=400,y=20,)
ret=Button (fenetre5,text="<<Retour",font=('Calistoga',8),bg="white")
ret.place(x=5,y=30,)


id = Label(fenetre5, text="Nom client",bg="#ffffff",fg="#000000").place(x=50, y=80)

idchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=160,y=80,)

nom = Label(fenetre5, text="Type poduit",bg="#ffffff",fg="#000000").place(x=450, y=80)

nomchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=550,y=80,)

prenom = Label(fenetre5, text="Nom magasinier",bg="#ffffff",fg="#000000").place(x=50, y=130)

prechamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=160,y=130,)

typro = Label(fenetre5, text="Quantité",bg="#ffffff",fg="#000000").place(x=450, y=130)

tprochamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=550,y=130,)

adresse = Label(fenetre5, text="Nom du produit",bg="#ffffff",fg="#000000").place(x=50, y=180)

adreschamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=160,y=180,)

tel = Label(fenetre5, text="Prix",bg="#ffffff",fg="#000000").place(x=450, y=180)

telchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=550,y=180,)

#les buton modification
pad= customtkinter.CTkButton(master=fenetre5,text="Valider",text_font=('Calistoga',11),command=quit,
                                      height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
pad.place(x=640,y=220)
#facture

texte=Label (fenetre5,text="Facture",font=('Calistoga',17),bg="white")
texte.place(x=400,y=250,)

modif= customtkinter.CTkButton(master=fenetre5,text="Modifier",text_font=('Calistoga',11),command=quit,
                                      height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
modif.place(x=200,y=590)
imp= customtkinter.CTkButton(master=fenetre5,text="Imprimmer",text_font=('Calistoga',11),command=quit,
                                      height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
imp.place(x=600,y=590)


fenetre5.mainloop()
