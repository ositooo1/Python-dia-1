import os
os.system("cls")
#1. Define una lista de diccionarios que  represente información personal. nombre,edad. Luego, accede a elementos específicos de la lista,  como el primer diccionario, el nombre  de la primera persona y la edad de la  segunda persona, para finalmente imprimir los resultados en la consola.
#1.2. Del punto 1, recorrer y mostrar k,v
#personas = [{'nombre':'Juan','edad':17},
#            {'nombre': 'Eric','edad':17}]

#print(personas[0])
#print(personas[0]['nombre'])
#print(personas[1]['edad'])
#for k in personas:
#    for v in k:
#        print(k,v)

# 2. Definir función, parámetros, retorno, capturar un valor o varios

#def jubilacion(age, name):  # La función debe definirse ANTES de llamarla
#    if age >= 65:
#        print(f'{name}, podés empezar a cobrar la jubilación, debido a que tu edad cumple los requerimientos')
#    else:
#        print(f"{name}, no podés cobrar la jubilación debido a que sos aún joven")

#name = input("Ingresa tu nombre: ")
#age = int(input("Poné tu edad: "))  

#jubilacion(age, name)  


#3. Contar palabras
#texto = input("Ingresá un texto: ")

#contador = 0
#en_palabra = False

#for letra in texto:
#    if letra != " ":  
#        if not en_palabra:  
#            contador += 1
#            en_palabra = True
#    else:
#        en_palabra = False  

#print(f"El texto tiene {contador} palabras")

#4. Verificación de Palíndromos
#texto = input("Ingresá una palabra o frase: ")

#texto_lower = texto.lower()


#texto_invertido = ""
#for letra in texto_lower:
 #   texto_invertido = letra + texto_invertido


#if texto_lower == texto_invertido:
#    print(f'"{texto}" ES un palíndromo')
#else:
#    print(f'"{texto}" NO es un palíndromo')


#5. Lambda para sumar, potencia
#sumar = lambda a, b: a + b
#potencia = lambda base, exponente: base ** exponente

#a = int(input("Ingresá el primer número: "))
#b = int(input("Ingresá el segundo número: "))

#print(f"Suma: {sumar(a, b)}")
#print(f"Potencia ({a}^{b}): {potencia(a, b)}")