nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
edad = int(edad)
print(f"Este es tu nombre: {nombre} esta es tu edad: {edad}")

diasvividos = 365 * edad
print(f"Usted ha vivido {diasvividos:,} dias") #  , con la coma se le dice al interprete  que agregue comas a la cantidad