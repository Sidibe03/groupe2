

import tkinter
from tkinter import *
from subprocess import call
root=Tk()
root.geometry("600x400")
root.resizable(FALSE,FALSE)

photo = PhotoImage(file = r"BIG STOCK1.png")

l1=Label(root, image= photo, border=0, relief=SUNKEN).place(x=220, y=100)

r= Label(root, text="Chargement ...", font =('Italic',20) )
r.place(x=200, y=250)

def main_windows():
    root.destroy()
    call(["python", "connexion.py"])
    # root.destroy()

    # fenetre.geometry("400x300")
    # fenetre.title("Connection")

root.after(1500, main_windows)
root.mainloop()