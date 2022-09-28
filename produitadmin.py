

#
#
# #page produit admin




from subprocess import call
from tkinter import *
import mysql.connector as mysql
from tkinter import Entry
import customtkinter as customtkinter
from tkinter import ttk
import pymysql as pymysql
from tkinter import messagebox


def acceuil():
    fenetre5.destroy()
    call(["python","accadmin.py"])




fenetre5=Tk()
fenetre5.title("Les produits Admin ")
fenetre5.geometry("1000x620")
fenetre5.resizable(False, False)
fenetre5.configure(bg="white")


texte=Label (fenetre5,text="Les Produits",font=('Calistoga',25),bg="white")
texte.place(x=200,y=57,)
ret=Button (fenetre5,text="<<Retour",font=('Calistoga',8),bg="white")
ret.place(x=5,y=30,)


#champ de recherche
texte = Label(fenetre5, text="Recherche", font=('Calistoga', 13), bg="white")
texte.place(x=500, y=60)
champ1 = Entry(fenetre5, bg="white", width=25, show="*", font=('Calistoga', 15))
champ1.place(x=620, y=60)

#affichage resultat
aff= ttk.Treeview(fenetre5, columns=(1,2,3,4,5,6),height=10,show="headings")
aff.place(x='',y='160',width=1000,height=400)

#nouveau fonction

def afficher():

    con = pymysql.connect(host="localhost", user="root", password="", database="bigstock")
    cursor=con.cursor()
    cursor.execute("select * from produit ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id,nom,quantite,date_arrive,fournisseur,telephone) in enumerate (records,start=1):
            aff.insert ("", "end", values=(id,nom,quantite,date_arrive,fournisseur,telephone))

    con.close()


#en tete
aff.heading(1,text="ID")
aff.heading(2,text="Nom")
aff.heading(3,text="Quantité")
aff.heading(4,text="Date d'arrivée")
aff.heading(5,text="Fournisseur")
aff.heading(6,text="Télephone Founiss")
#dimension des colonnes
aff.column(1,width=10)
aff.column(2,width=10)
aff.column(3,width=10)
aff.column(4,width=10)
aff.column(5,width=10)
aff.column(6,width=10)

#suivante et precedente
pad=Button(master=fenetre5,text="<<Précedente",font=('Calistoga',11),command=quit,fg="#000000",
                                      width=11,bg="#ffffff")
pad.place(x=700,y=580)

pad=Button(master=fenetre5,text="Suivante>>",font=('Calistoga',11),command=quit,fg="#000000",
                                     width=10,bg="#ffffff")
pad.place(x=850,y=580)


afficher()
fenetre5.mainloop()


