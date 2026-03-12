import os
os.system("cls")


#1. Escribe un programa que imprima un  mensaje personalizado en la pantalla utilizando la función print().

#print("¡Hola! Bienvenido a la programación en Python.")

"""2. Escribe un programa que le pida al usuario
su nombre y luego lo imprima en la pantalla."""

"""nombre = input("Ingresa tu nombre:")
print(f"Buenas Buenas {nombre}")"""

#3. Escribe un programa que le pida al usuario dos números y luego imprima la suma de esos números.

"""num1 = float(input("Pone el primer numero:"))
num2 = float(input("Pone el segundo numero:"))
suma = num1 + num2
resta = num1 - num2
division = num1/num2
multiplicacion = num1*num2
print(f"La suma da {suma}")
print(f"La resta da {resta}")
print(f"La division da {division}")
print(f"La multiplicacion da {multiplicacion}")"""


#4. Escribe un programa que tome dos cadenas de texto (strings) como entrada del usuario y lasconcatene, luego imprime el resultado."""

"""nombre1 = input("pone aca tu primer nombre:")
nombre2 = input("pone aca tu segundo nombre:")
print(f"Hola {nombre1} {nombre2}")"""


#5. Escribe un programa que compare dos números y muestre si son iguales o no utilizando operadores de comparación (por ejemplo, ==, !=)
"""num1 = input("Pone aca el primer numero:")
num2 = input("Pone aca tu segundo numero:")
if num1==num2:
    print(f"Son iguales")
else:
    print(f"No son iguales")"""

#6. Escribe un programa que utilice operadores de asignación para realizar operaciones como  incrementar o decrementar el valor de una variable.

"""contador = int(input("Pone el numero que quieras:"))
print(f"Tu numero original es {contador}")
contador += 2
print(f"El nuevo numero mas grande es {contador}")
contador -= 4
print(f"El nuevo numero mas chico es {contador}")"""

#7. crear un programa que le pida al usuario
#nombre, edad y ciudad de residencia, realizar
#cálculos basados en la edad, y luego mostrará
#la información en pantalla 
# Pedir al usuario que ingrese su nombre
# Pedir al usuario que ingrese su edad
# Pedir al usuario que ingrese su ciudad de residencia
# Calcular el año de nacimiento
# Saludar al usuario y mostrar la información
# Comprobar si la edad es mayor de 18 años
# Comprobar si la edad es un múltiplo de 5).

"""nombre = input("Nombre:")
edad = int(input("Edad:"))
ciudad = input("Ciudad Donde Vivis:")
año = 2026 - edad
print(f"Buenas Tardes {nombre}, Nacido en {ciudad} en el año {año} ")
if edad<18:
    print("Eres menor de edad")
else:    print("Eres mayor de edad")
if edad%5==0:
    print("Tu edad es un multiplo de 5")
"""

#8.  crearemos un programa que verifica si un número ingresado por el usuario es positivo, negativo o cero, y también si es un número par o impar.

"""num = int(input("Pone un numero:"))
if num > 0:
    print(f"Tu numero es positivo")
if num == 0:
    print(f"Tu numero es 0")
if num < 0:
    print(f"Tu numero es negativo")
if num%2==0:
    print(f"Tu numero es par")
else:
    print(f"Tu numero es impar")"""