import os
from random import randint
os.system('cls')



#5- Juego de adivinanza de números:
#Genera un número aleatorio entre 1 y 100.
#Pide al usuario que adivine el número.
#Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
#Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
#Muestra el número de intentos necesarios para adivinar.



num = randint(1,100)
intentos = 0
jugador = int(input("Ingrese un numero del 1 al 100:"))
intentos += 1

while jugador != num:
    if jugador<num:
        print("Probar mas alto")
    if jugador>num:
        print("Probar mas bajo")
    jugador = int(input("Ingrese un numero del 1 al 100:"))
    intentos += 1
if jugador == num:
    print(f"Le pegaste, despues de {intentos} intentos")