import os
os.system('cls')

#3- Generador de secuencia Fibonacci:
#Pide al usuario que ingrese un número entero positivo.
#Genera los primeros n números de la secuencia Fibonacci, donde n es el número ingresado por el usuario.
#Muestra la secuencia Fibonacci resultante.

n = int(input("Ingrese un numero entero positivo: "))

fibonacci = [0, 1]

for i in range(n - 2):
    nuevo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(nuevo)

print(fibonacci)

    
