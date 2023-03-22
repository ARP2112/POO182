from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel=ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

# Pestana1:Agregar Usuarios
titulo= Label(pestana1, text="Registro de Usuarios", fg="blue", font=("Modern",18)).pack()

varNom= tk.StringVar()
Ib1Nom= Label(pestana1, text="Nombre: ").pack()
txtNom= Entry(pestana1, textVariable=varNom).pack()

varCor= tk.StringVar()
Ib1Cor= Label(pestana1, text="Correo: ").pack()
txtCor= Entry(pestana1, textVariable=varCor).pack()

varCon= tk.StringVar()
Ib1Con= Label(pestana1, text="Contraseña: ").pack()
txtCon= Entry(pestana1, textVariable=varCon).pack()

btnGuardar= Button(pestana1, text='Guardar usuario').pack()

panel.add(pestana1, text="Agregar Usarios")
panel.add(pestana2, text="Buscar Usarios")
panel.add(pestana3, text="Consultar Usarios")
panel.add(pestana4, text="Actualizar Usarios")


Ventana.mainloop() 
