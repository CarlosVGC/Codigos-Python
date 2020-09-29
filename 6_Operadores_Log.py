"""
Operadores Logicos proporcionan un resultado a partir de que se cumpla una cierta condicion, 
producen un resultado booleano falso o verdadero Existen tres operadores lógicos los cuales son:
Y (AND) Ambos sean verdaderos para que el res sea verdadero
O (OR) Se requiere que uno sea verdadero
Negacion (NOT) Negación invierte

prioridad:
NOT
AND
OR

prioridades de los operadores:
()
**
*, / , //, mod, not
+, -, and
>,<, ==, >=, <= , != , or 
"""

n1 = 10
n2 = 20
n3 = 30

res = ((n1 < n2) and (n2 < n3))
print(n1 < n2 , "and", n2<n3," : ", res)
res = ((n1 > n2) and (n2 < n3))
print(n1 > n2 , "and", n2<n3," : ", res)
res = ((n1 > n2) or (n2 < n3))
print(n1 > n2 , "or", n2<n3," : ", res)

resnegado = not res
print("Resultado negado: ",res, resnegado)