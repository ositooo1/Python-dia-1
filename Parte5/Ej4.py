import os
os.system('cls')

#4- Validador de contraseña:
#Solicita al usuario que cree una contraseña.
#Verifica si la contraseña cumple con los siguientes criterios:
#Tiene al menos 8 caracteres de longitud.
#Contiene al menos una letra mayúscula y una letra minúscula.
#Tiene al menos un número.
#Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
#Informa al usuario si la contraseña es válida o no.


contra = input("Ingrese una contra segura:")
upper = False
lower = False
num = False
long = False
caracter_special = False
caracteres = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-="]
for i in contra:
    if len(contra) >= 8:
        long = True
    if i.isupper():
        upper = True
    if i.islower():
        lower = True    
    if i.isdigit():
        num = True
    if i in caracteres:
        caracter_special = True
if upper and lower and num and long and caracter_special:
    print("La contra es segura")
if not upper:
    print("La contra debe tener almenos una mayuscula")
if not lower:
    print("La contra debe tener almenos una minuscula")
if not num:
    print("La contra debe tener almenos un numero")
if not long:
    print("La contra debe tener almenos 8 caracteres")
if not caracter_special:
    print("La contra debe tener almenos un caracter especial")