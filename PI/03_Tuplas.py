'''
Las tuplas son listas inmutables
no permitens añadir, mover o eliminar elementos (append, extend, remove)
Permiten extraer porcione, el resultado es una tupla nueva
Permiten busquedas
permiten comprobar si un elemento se encuentra en la tupla

Sus principales ventajas son respecto a las listas:
mas rapidas
menos espacio 
formatean Strings
pueden utilizarse como claves en un diccionario

'''

def listas():
    nombreTupla = ('elem1', 'elem2', 3, 4)
    print(nombreTupla[1])
    lista=list(nombreTupla) # Se transforma una tupla en lista 
    listaATupla = tuple(lista) #Se transforma una lista a tupla 
    print(lista)
    print(nombreTupla)
    print(listaATupla)

    print("elem1" in nombreTupla) #Si esta el elemento en la tupla se imprime
    print(nombreTupla.count('elem1')) #cuenta numero de elementos
    print(len(nombreTupla))#devulve el tamaño de la tupla
    
    tuplanueva = 'Juan',13,10,2000 # Se pueden crear tuplas sin necesidad de poner parentesis (empaquetado de tupla)
    print(tuplanueva)

    nombre, dia, mes, anio = tuplanueva  #desempaquetado de tupla asigna a cada variable lo contenido en la tupla
    print(nombre)
    print(dia)
    print(mes)
    print(anio)



























listas()