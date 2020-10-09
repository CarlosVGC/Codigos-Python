def suma(num1, num2):
    return num1+num2

num1 = 3
num2 = 4

res=suma(num1, num2)

print(res)

#listas
NombreLista = ['elemento1', 'elemento2', 3, 4]
for n in NombreLista:
    print(n)
print(len(NombreLista)) # longitud de una lista

NombreLista.append("Append") #inserta un elemento al finl de la lista
NombreLista.insert(2,"Insert") #Inserta elemento en posicion deseada
print(NombreLista)
NombreLista.extend(["Lista21", "Lista22", 23])#concatena una lista con contra lista
print(NombreLista)

print(NombreLista.index(23))#regresa el numero en el que se encuentra 0-n 

print('elemento2' in NombreLista) #regresa false o True dependiendo de si se encuentra en la lista

#para la eliminacion de un elemento en la cadena
NombreLista.remove('elemento2') #elimina los elementos 'elemento2'
NombreLista.pop() #elimina el ultimo elemento agregado

lista1=[1,2,3]
lista2 = ['1','2','3']
lista3 = lista1 + lista2 #concatena 2 listas
print(lista3)

lista3=lista3*3
print(lista3)
