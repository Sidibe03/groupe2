

from tkinter import *



fenetre=Tk()
fenetre.title("page d'acceil Magasinier")
fenetre.geometry("1000x620")
fenetre.resizable(False,False)
fenetre.configure(bg="white")


#menu
menu=Frame(fenetre,background="#395fb8",width="250",height="425")
menu.place(x=745,y=190)

#acceuil
acc=Frame(fenetre,background="#d9d9d9",width="1000",height="185")
acc.place(x="",y="")

#corps
acc=Frame(fenetre,background="#d9d9d9",width="740",height="425")
acc.place(x="",y="190")

prod=Button(acc,text="Produits",bg="#395fb8",fg="white",font=('',25,),width="15",height="3")
prod.place(x="35",y="20")
prod=Button(acc,text="Livraisons",bg="#395fb8",fg="white",font=('',25,),width="15",height="3")
prod.place(x="400",y="20")

prod=Button(acc,text="Fournisseurs",bg="#395fb8",fg="white",font=('',25,),width="15",height="3")
prod.place(x="35",y="200")
prod=Button(acc,text="Statistique",bg="#395fb8",fg="white",font=('',25,),width="15",height="3")
prod.place(x="400",y="200")

#copyrith
preven=Label(acc,text="Copyright @ 0101 par Groupe 2/ODC")
preven.place(x="250",y="400")


fenetre.mainloop()