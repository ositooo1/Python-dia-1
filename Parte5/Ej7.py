import os

os.system("cls")


# 7- Calculadora de descuento de compra:
# Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
# Calcula el precio final después del descuento.
# Muestra el precio final al usuario.


precio = float(input("Ingrese el precio del articulo:"))
descuento = float(input("Ingrese el porcentaje del descuento:"))
precio_final = precio - (precio * descuento / 100)
print(f"El precio final es de {precio_final}")
