from tkinter import Tk,Button,Frame

#1. Generar una ventana
ventana=Tk()
ventana.title("Ejemplo 3 Frames")
ventana.geometry("600x400")

#2. Agregar Frames
seccion1=Frame(ventana,bg="pink")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="grey")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="blue")
seccion3.pack(expand=True,fill='both')

#3. Agregamos los botones
botonNegro= Button(seccion1,text="Boton Negro",fg="black")
botonNegro.place(x=60,y=60,width=100,height=30)

botonNegro= Button(seccion2,text="Boton Negro",fg="black")
botonNegro.grid(row=0,column=0)

botonNegro= Button(seccion2,text="Boton Negro",fg="black")
botonNegro.grid(row=1,column=1)


botonNegro= Button(seccion3,text="Boton Negro",fg="black")
botonNegro.pack()




#Metodo Main para ejecutar la ventana
ventana.mainloop()
