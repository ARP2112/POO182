from tkinter import Tk,Frame
import tkinter as tk

ventana=Tk()
ventana.title("INGRESAR:")
ventana.geometry("600x400")

seccion1=Frame(ventana, bg="pink")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana, bg="pink")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana, bg="pink")
seccion3.pack(expand=True,fill='both')

seccion4=Frame(ventana, bg="pink")
seccion4.pack(expand=True,fill='both')

seccion5=Frame(ventana, bg="pink")
seccion5.pack(expand=True,fill='both')

Nombre=tk.Label(seccion1, text="Nombre: ")
Nombre.place(x=20, y=50)

ApellidoP=tk.Label(seccion2, text="Apellido Paterno:")
ApellidoP.place(x=20, y=50)

ApellidoM=tk.Label(seccion3, text="Apellido Materno: ")
ApellidoM.place(x=20, y=50)

Año_Nac=tk.Label(seccion4, text="Año de Nacimiento:")
Año_Nac.place(x=20, y=50)

Carrera=tk.Label(seccion5, text="Carrera:")
Carrera.place(x=20, y=50)
# Introducir Datos
Nombre1=tk.Entry(seccion1, width=30)
Nombre1.place(x=170, y=50)

ApellidoP1=tk.Entry(seccion2, width=50)
ApellidoP1.place(x=190, y=100)

ApellidoM1=tk.Entry(seccion3, width=50)
ApellidoM1.place(x=190, y=100)

Año_Nac1=tk.Entry(seccion4, width=30)
Año_Nac1.place(x=170, y=50)

Carrera1=tk.Entry(seccion5, width=30)
Carrera1.place(x=170, y=50)




ventana.mainloop()