from Personaje import *

print(" ")
print("### Solicitud Datos del Heroe ###")
especieH= input("Escribe la especie del Heroe: ")
nombreH= input("Escribe el nombre del Heroe: ")
alturaH= float(input("Escribe la altura del Heroe: "))
recargarH= int(input("Ingresa la cantidad de balas para el Heroe: "))

print(" ")
print("### Solicitud Datos del Villano ###")
especieV= input("Ecribe la especie del Villano: ")
nombreV= input("Ecribe el nombre del Villano: ")
alturaV= float(input("Escribe la altura del Villano: "))
recargarV= int(input("Ingrese la cantidad de balas para el Villano: "))

#2. Creamos los objetos
Heroe=Personaje(especieH, nombreH, alturaH)
Villano= Personaje(especieV, nombreV, alturaV)

#3. Usamos los atributos Heroe y Villano

print(" ")
print("### Metodos y Atributos del Heroe: ###")
print("El Heroe se llama "+ Heroe.nombre)
print("Pertenece a la especie "+ Heroe.especie)
print("Y tiene una altura de "+ str(Heroe.altura))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargarH)


print(" ")
print("### Metodos y Atributos del Villano: ###")
print("El Villano se llama "+ Villano.nombre)
print("Pertenece a la especie "+ Villano.especie)
print("Y tiene una altura de "+ str(Villano.altura))


Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargarV)