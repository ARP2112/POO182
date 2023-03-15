from tkinter import Tk,Button,Frame

ventana=Tk()
ventana.title("INGRESAR:")
ventana.geometry("15x30")

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

Nombre=Tk.Label(seccion1, text="Nombre: ")
Nombre.place(x=20, y=50)

ApellidoP=Tk.Label(seccion2, text="Apellido Paterno: ")
ApellidoP.place(x=20, y=100)

ApellidoM=Tk.Label(seccion3, text="Apellido Paterno: ")
ApellidoM.place(x=20, y=50)

Año_Nacimiento=Tk.Label(seccion4, text="Apellido Materno: ")
Año_Nacimiento.place(x=20, y=100)

Carrera=Tk.Label(seccion5, text="Carrera: ")
Carrera.place(x=20, y=50)



ventana.mainloop()
