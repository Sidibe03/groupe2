

# creation de compte
import tkinter
from subprocess import call
from tkinter import *
from tkinter import ttk
import mysql.connector
import mysql.connector as mysql

root = Tk()
root.title("Création de compte")
root.geometry("1000x620")
root.resizable(False, False)
root.configure(bg="white")

#connexion a la BD
def insert():
    nom = nomchamp.get();
    prenom = prenomchamp.get();
    telephone = pwdchamp.get();
    email=emailchamp.get();

    con = mysql.connect(host="localhost", user="root", password="", database="bigstock")
    cursor = con.cursor()
    cursor.execute("insert into magasinier values ('" + nom + "','" + prenom + "','" + telephone + "','" + email + "') ")
    cursor.execute("commit");

    con.close();


frame1 = Frame(root, bg="#d9d9d9", width=600, height=400)
frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
"""
def valide():
        nom = nomchamp.get()
        prenom = prenomchamp.get()
        email = emailchamp.get()
        pwd = pwdchamp.get()
        cfm = cfmchamp.get()


    if(no m=="" or preno m=="" or emai l=="" or pw d=="" or cf m=="" ):
         MessageBox.showinfo("Echec", "Tous les champs sont requis")

    elif(pwd! =cfm):
            MessageBox.showinfo("Echec" ,"veillez saisir un mot de passe correcte")
    else:
            con = mysql.connect(host="", user="", password="", database="")
            cursor = con.cursor()
            cursor.execute \
                ("insert into "" values(' "+ nom +"','" + prenom + "','" + email + "','" + pwd + "',,'" + cfm + "')")
            cursor.execute("commit")
            MessageBox.showinfo("Compte", "")
            con.close()
"""
t1 = Label(frame1, text="BigStock", font=('Italic', 16), bg="#d9d9d9").place(x=260, y=30)

t2 = Label(frame1, text="Création de compte", font=('Italic', 16), bg="#d9d9d9").place(x=200, y=80)

nom = Label(frame1, text="Nom :", bg="#d9d9d9").place(x=70, y=150)
nomchamp = Entry(frame1, bg="#B1B8C8")
nomchamp.place(x=140, y=150)

prenom = Label(frame1, text="Prénom :", bg="#d9d9d9").place(x=70, y=180)
prenomchamp = Entry(frame1, bg="#B1B8C8")
prenomchamp.place(x=140, y=180)

email = Label(frame1, text="Email :", bg="#d9d9d9").place(x=70, y=210)
emailchamp = Entry(frame1, bg="#B1B8C8")
emailchamp.place(x=140, y=210)

pwd = Label(frame1, text="Password :", bg="#d9d9d9").place(x=360, y=150)
pwdchamp = Entry(frame1, bg="#B1B8C8")
pwdchamp.place(x=440, y=150)

cfm = Label(frame1, text="Confirm :", bg="#d9d9d9").place(x=360, y=180)
cfmchamp = Entry(frame1, bg="#B1B8C8")
cfmchamp.place(x=440, y=180)

stt = Label(frame1, text="Statut :", bg="#d9d9d9").place(x=360, y=210)

check1 = tkinter.Checkbutton(frame1, text="Mag", bg="#d9d9d9")
check1.place(x=445, y=210)

check2 = tkinter.Checkbutton(frame1, text="Admin", bg="#d9d9d9")
check2.place(x=510, y=210)

vld = Button(frame1, text="Validé", command=insert)
vld.place(x=270, y=300)

root.mainloop()
