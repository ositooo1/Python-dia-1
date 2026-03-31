import os
os.system('cls')

#1- Calculadora de índice de masa corporal (IMC):
#- Solicita al usuario que ingrese su peso en kg y su altura en metros.
#- Calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
#- Muestra el IMC calculado y una categoría de peso según el IMC (talla s, talla m, talla l, talla xl).


peso = float(input("Ingrese su peso en KG:"))
altura = float(input("Ingrese su altura en Metros(Va punto no coma):"))
IMC = float(peso / (altura * altura))
print(f"Tu IMC es {IMC}")
if IMC<18.5:
    print(f"Sos talla S")
if 18.5<IMC<24.9:
    print(f"Tu talla es M")
if 25<IMC<29.9:
    print(f"Tu talla es L")
if IMC>30:
    print(f"Tu talla es XL")