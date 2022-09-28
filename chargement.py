




import tkinter
from subprocess import call
from tkinter import *
from PIL import Image
from PIL import Image,ImageTk
import customtkinter as customtkinter

root = Tk()
root.title("splashscreen")
root.geometry("600x400")
root.resizable(FALSE,FALSE)

photo = PhotoImage(file = r"BIG STOCK1.png")

l1=Label(root, image= photo, border=0, relief=SUNKEN).place(x=220, y=100)

r= Label(root, text="Chargement ...", font =('Italic',15) )
r.place(x=430, y=360)

def connexion():

    root.destroy()
    call(["python", "connexion.py"])

root.after(1500, connexion)
root.mainloop()
