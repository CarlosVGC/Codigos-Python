# Ejemplo de uso de diccionarios
'''
Estructuras que permite almacenar datos en un diccionario clave: valor
Los elementos almacenados no estan ordenados, el orden es indiferente a la hora de almacenar
informacion en un diccionario
se pueden almacenar dentro de ellos:variables, listas, tuplas, diccionarios,
'''

def dic():
    diccionario = {'Clave': 'Valor'} #Ejemplo de estructura diccionario
    print(diccionario) #Imprime el diccionario

    preferencias = {'Carlos': 'C', 'Rocio': 'Python', 'Pedro': 'Java'}
    print(preferencias['Carlos'])
    preferencias['Juan'] = 'Ruby' #Agregando elemento en un diccionario
    print(preferencias)
    preferencias['Juan'] = 'Java' #Modificacando un elemento en un diccionario
    print(preferencias)
    del preferencias['Pedro'] #Eliminando un elemento del diccionario
    print(preferencias)


def dic2(): #ejemplo de como se realiza un diccionario con listas
    tupla = ['Jorge','Juan','Pedro','Rodrigo','Elizabeth']
    ndic = {tupla[0]: 'c', tupla[1]: 'Java'}
    print(ndic)

def dic3(): #diccionarios con listas, tuplas, diccionarios
    pais = {'Mexico': ['Toluca','Ecatepec', 'Metepec'],
            'EUA': ('Dakota', 'Salt Lake City', 'New York'),
            'España':{'Madrid': 'Santiago', 'Barcelona': ['Versalles', 'Milán']
                     }}
    print(pais.keys())
    print(pais.values())
    print(len(pais))

dic()
dic2()
dic3()