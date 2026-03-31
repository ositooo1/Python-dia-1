import os
os.system('cls')
#2- Conversor de temperaturas:
#Pide al usuario que ingrese una temperatura en grados Celsius.
#Convierte la temperatura a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
#Imprime la temperatura en grados Fahrenheit.

celsius = float(input("Ingrese su temperatura en grados Celsius:"))
fahrenheit = float((celsius * 9/5) + 32)
print(f"Tu temperatura en grados Fahrenheit es {fahrenheit}")