#Intercambio de valores usando 3 variables

n1 = float(input("Ingresa el valor 1: "))
n2 = float(input("Ingresa el valor 2: "))

print(f"Los valores antes del intercambio son: n1: {n1} n2: {n2}")

aux = n1
n1 = n2
n2 = aux

print(f"Los valores despues del intercambio son: n1: {n1} n2: {n2}")
