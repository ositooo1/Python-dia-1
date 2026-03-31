import os
os.system("cls")
#1. Escribe un programa que identifique el color de un objeto y muestre un mensaje según el color.
#color = input("Ingresa el color del objeto:")
#if color.lower() == "rojo":
#    print("El objeto es rojo")
#elif color.lower() == "azul":
#    print("El objeto es azul")
#elif color.lower() == "verde":
#    print("El color es verde")
#else:    print(f"No se reconoce el color del objeto")

#2. Escribe un programa que muestre los números del 0 al 4 usando un ciclo while.

#count = 0
#while count < 5:
#    print(f"El número es: {count}")
#    count += 1 

# 2.1. Escribe un programa que solicita al usuario que ingrese números enteros positivos y muestre la suma de esos números. La entrada de números continuará hasta que el usuario ingrese un  número negativo, momento en el que el programa  mostrará la suma total
#suma = 0
#while True:
#    numero = int(input("Ingresa un número entero positivo (o un número negativo para finalizar): "))
#    if numero < 0:
#        break
#    suma += numero
#print(f"La suma total es: {suma}")


#3.Escribe un programa que muestra la primer, última u otra letra de una cadena de carcateres, inclusive una rebanada.
#cadena = input("Ingrese una palabra:")
#print(f"La primer letra es: {cadena[0]}")
#print(f"La ultima letra es: {cadena[-1]}")
#print(f"La letra en la mitad es: {cadena[len(cadena)//2]}") 

#4.Crear una lista de frutas y mostrar en consola algunas frutas de la lista, también por rebanadas.
#import random
#frutas = ["manzana", "banana", "naranja", "uva", "pera"]
#print(f"La primer fruta es: {frutas[0]}")
#print(f"La última fruta es: {frutas[-1]}")
#print(f"Una random es: {random.choice(frutas)}")

#5. Escribe un programa que recorra una lista de  frutas y muestre cada fruta.
#5.1 Agregar otras frutas a la lista.
#5.2 Escribe un programa verifique si una fruta  específica está en una lista de frutas y muestra un mensaje correspondiente.
#frutas = ["manzana", "banana", "naranja", "uva", "pera"]

#for fruta in frutas:
#    print(f"Fruta: {fruta}")
    
#frutas.append(input("Agrega una fruta a la lista: "))
#print("Lista actualizada de frutas:")
#for fruta in frutas:
#    print(f"Fruta: {fruta}")
#frutas_especificas= input("Ingresa el nombre de una fruta para ver si ya esta: ")
#if frutas_especificas in frutas:
#    print(f"La fruta {frutas_especificas} si esta en la lista")
#else:
#    print(f"La fruta {frutas_especificas} no esta en la lista")

#6. Escribe un programa que recorra una lista de números y muestre si cada número es par o impar.
#numeros = [1,2,3,4,5,6,7,8,9,10]
#for numero in numeros:
#    if numero%2==0:
#        print(f"El numero {numero} es par")
#    else:        print(f"El numero {numero} es impar")

#7. Escribe un programa que recorra una cadena de  texto y cuente cuántas veces aparece la letra 'a' en la cadena.
#palabra = input("Escribe una palabra:")
#contador = 0
#for letra in palabra:
#    if letra.lower() == "a":
#        contador += 1
#print(f"La letra 'a' aparece {contador} veces en la palabra.")
#8. Integrador: Escribe un programa que permita a un usuario crear una lista de nombres. El programa continuará pidiendo nombres hasta que el usuario ingrese "fin". Luego,  el programa mostrará la lista de nombres en orden alfabético, indicará cuántos nombres empiezan con la letra 'A' o 'E',  y mostrará si un nombre específico está en la lista.

#lista_nombres = []
#while True:
#    nombre = input("Ingresa un nombre (o 'fin' para terminar): ")
#    if nombre.lower() == "fin":
#        break
#    lista_nombres.append(nombre)
#lista_nombres.sort()
#print("Lista de nombres en orden alfabético:")
#for nombre in lista_nombres:
#    print(f"- {nombre}")
#contador_a = sum(1 for nombre in lista_nombres if nombre.lower().startswith(('a', 'e')))
#print(f"Nombres que empiezan con 'A' o 'E': {contador_a}")