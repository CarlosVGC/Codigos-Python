#Enteros: 1-9
#Cadenas    "cadena" o 'cadena' se puede hacer con comillas simples o dobles
#Flotantes: 1.1 -9.9
#Booleanos: True False


x: str = True # : str es un "hint" una pista a lo que apuntará la variable, se puede usar otro tipo de variable, solo es un indicador no define la variable
print(x, end='') #se le quita el formato del salto de linea

print(type(x)) #las variables apuntan a un tipo de memoria

#manejo de cadenas
grupofav = "Ace of Base"
comentario = "La mejor agrupacion"
print("Mi grupo favorito es: "+grupofav+ " "+ comentario) #se puede concatenar sin "+" si son cadenas consecutivas
print("Mi grupo favorito es:", grupofav, comentario) #con la coma se agrega un espacio a la concatenacion
print(f'Mi grupo favorito es: {grupofav} {comentario}') #otro tipo de formateo para impresion cadenas

num1, num2 = 1, 2
print(str(num1)+str(num2))
