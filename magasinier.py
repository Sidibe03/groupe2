


#page des  magasiniers pour admin


from subprocess import call
from tkinter import *
import pymysql as pymysql
from tkinter import ttk,Entry
import customtkinter as customtkinter
# from tkinter import ttk
#import mysql.connector
from tkinter import messagebox



def prodmag():
    fenetre5.destroy()
    call(["python","accadmin.py"])



fenetre5=Tk()
fenetre5.title("Modification des magasinier ")
fenetre5.geometry("1000x620")
fenetre5.resizable(False, False)
fenetre5.configure(bg="white")


#les fonctions

def afficher():

    con = pymysql.connect(host="localhost", user="root", password="", database="bigstock")
    cursor=con.cursor()
    cursor.execute("select * from magasinier ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id,nom,prenom,date,adresse,telephone) in enumerate (records,start=1):
            aff.insert ("", "end", values=(id,nom,prenom,date,adresse,telephone))

    con.close()


texte=Label (fenetre5,text="Les Magasiniers",font=('Calistoga',25),bg="white")
texte.place(x=400,y=20,)
ret=Button (fenetre5,text="<<Retour",font=('Calistoga',8),bg="white",command=prodmag)
ret.place(x=5,y=30,)



id = Label(fenetre5, text="ID",bg="#ffffff",fg="#000000").place(x=50, y=80)

idchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=50,y=100,)

nom = Label(fenetre5, text="Nom",bg="#ffffff",fg="#000000").place(x=50, y=130)

nomchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=50,y=150,)

prenom = Label(fenetre5, text="Prénom",bg="#ffffff",fg="#000000").place(x=50, y=180)

prechamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=50,y=210,)

typro = Label(fenetre5, text="Date arrivée",bg="#ffffff",fg="#000000").place(x=340, y=80)

tprochamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=340,y=100,)

adresse = Label(fenetre5, text="Adresse",bg="#ffffff",fg="#000000").place(x=340, y=130)

adreschamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=340,y=150,)

tel = Label(fenetre5, text="Téléphone",bg="#ffffff",fg="#000000").place(x=340, y=180)

telchamp=Entry(fenetre5,bg="white",width=25,font=('Calistoga',12)).place(x=340,y=210,)

#affichage resultat
aff= ttk.Treeview(fenetre5, columns=(1,2,3,4,5,6),height=10,show="headings")
aff.place(x='',y='290',width=1000,height=280)
#en tete
aff.heading(1,text="ID")
aff.heading(2,text="Nom")
aff.heading(3,text="Prénom")
aff.heading(4,text="Date arrivée")
aff.heading(5,text="Téléphone")
aff.heading(6,text="Adresse")
#dimension des colonnes
aff.column(1,width=10)
aff.column(2,width=10)
aff.column(3,width=10)
aff.column(4,width=10)
aff.column(5,width=10)
aff.column(6,width=10)
#les buton modification
pad= customtkinter.CTkButton(master=fenetre5,text="Ajouter",text_font=('Calistoga',11),command=quit,
                                      height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
pad.place(x=150,y=250)
pad= customtkinter.CTkButton(master=fenetre5,text="Supprimer",text_font=('Calistoga',11),command=quit,
                                      height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
pad.place(x=300,y=250)
pad= customtkinter.CTkButton(master=fenetre5,text="Modifier",text_font=('Calistoga',11),command=quit,
                                      height=20,width=100,border_width=1,corner_radius=3,fg_color="#319BFE")
pad.place(x=450,y=250)

#suivante et precedente
pad=Button(master=fenetre5,text="<<Précedente",font=('Calistoga',11),command=quit,fg="#000000",
                                      width=11,bg="#ffffff")
pad.place(x=700,y=580)

pad=Button(master=fenetre5,text="Suivante>>",font=('Calistoga',11),command=quit,fg="#000000",
                                     width=10,bg="#ffffff")
pad.place(x=850,y=580)



fenetre5.mainloop()
