from cuentaDeAhorros import *
from os import system

import msvcrt


"""
integrantes:
 Giania Valeria Caicedo 
 Ivan Andres Santacruz
 Nubia Vanessa Lopez
"""
#test

#  ingresando el  usuario 
usuario1=cuenta("Andres","santacruz","10832663",22,300000)

# prueba de gets 
system("cls")
print("verificando si el usuario se ingreso\n ")
print("el  usuario es "+usuario1.getNombre(),usuario1.getApellido())
print("\n\nPresione una tecla para continuar...")
msvcrt.getch()
system("cls")


# prueba de metodo mostrar
print( "resumen de la cuenta y el usuario")
print(usuario1.mostrar())
print("\n\nPresione una tecla para continuar...")
msvcrt.getch()
system("cls")


# prueba de sets para actulizar el nombre Y edad 
usuario1.setNombre("juan")
usuario1.setEdad(44)
print( "Actulizacion por atibutos \n")
print( "el nombre y la edad an sido actualizados",usuario1.getNombre(),usuario1.getApellido(),"su edad es ",usuario1.getEdad(),"años")
print("\n\nPresione una tecla para continuar...")
msvcrt.getch()
system("cls")
#prueba metodos ingresar 

print ("Consignacion de dinero\n")
print(usuario1.ingresar(200000))
print("\n\nPresione una tecla para continuar...")
msvcrt.getch()
system("cls")
#prueba metodo retirar
print ("retiro de dinero\n")
print(usuario1.retirar(100000))