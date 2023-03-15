from tkinter import Tk,Frame, Label

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

Nombre=Tk.Label(seccion1, text="Nombre: ")
Nombre.place(x=20, y=50)

ventana.mainloop()
