#Condicional anidada básica
edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad < 125: # 0 <= edad < 120
    if edad >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")
else:
    print("Su edad no es correcta verifiquela")
