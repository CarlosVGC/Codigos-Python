"""
Existen
Breapoints clik derecho edit breakpoint , se pone para poner una condicion
    Expression en break point se agrega con click derecho una expresion a validad
    Hit count cuantas veces pasa el debug por ahi
    Log Message expresion como La suma es {resultado}
Watches  Se sigue una variable ver su valor a lo largo de la ejecución del programa
Raised Exceptions se detiene el debug si encuentra errores de mayor magnitud
Uncaught Exceptions se detiene el debug si encuentra errores
"""

n1 = 10
n2 = 2

resultado = n1 + n2
print("La suma es: ", resultado) # se concatena entero con coma (,)
resultado = n1 - n2
print("La resta es: ",  resultado)
resultado = n1 * n2
print("La multiplicacion es: ",  resultado)
resultado = n1 / n2
print("La division es: ",  resultado)
resultado = n1 // n2
print("La division entera es: ",  resultado)
resultado = n1 % n2
print("El modulo es: ",  resultado)
resultado = n1 ** n2
print("El exponente es: ",  resultado)

#haciendo expresion matematica

res = (3**3)*(13/5*(2*4))
print("El resultado es: ", res)