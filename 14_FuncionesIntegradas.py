#Ejemplo de funciones integradas en Python
"""
bin()  transforma un numero a binario
hex() hexadecimal
abs() absoluto
round() Redondear
eval()  evaluar
"""
numero = bin(15083)
print(numero)
print(f"El numero decimal 15083 en binario es: {numero}")
numero2 = int('0b1010', 2)
print(f"El numero  binario 0b1010 es: {numero2} en decimal")

numero3 =hex(10)
print(f"El numero 10 en hexadecimal es: {numero3}")

numero4 = int('0xa', 16)
print(f"El numero decimal de 'a' es: {numero4}")

numero5 = abs(-100)
print(f"El valor absoluto de -100 es: {numero5}")

numero6 = round(7.6)
print(f"redondeo de 7.6 es {numero6}")

numero7 = eval('5+6')
print(f"eval(5+6) {numero7}")

