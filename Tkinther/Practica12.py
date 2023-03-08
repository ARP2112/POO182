from tkinter import Tk, Button, Frame, messagebox
import tkinter as tk

ventana=Tk()
ventana.title("Login")
ventana.geometry("400x300")

seccion1=Frame(ventana, bg="#f7badf")
seccion1.pack(expand=True,fill='both')

Correo=tk.Label(seccion1, text="Ingresa tu Correo: ")
Correo.place(x=20, y=50)
Contraseña=tk.Label(seccion1, text="Ingresa tu Contraseña: ")
Contraseña.place(x=20, y=100)

Correo1=tk.Entry(seccion1, width=30)
Correo1.place(x=170, y=50)
contraseña1=tk.Entry(seccion1, width=30)
contraseña1.place(x=170, y=100)


botonIngresar=Button(seccion1,text="Ingresar", bg="white", fg="black")
botonIngresar.place(x=50, y=250, width=100, height=30)

ventana.mainloop()
