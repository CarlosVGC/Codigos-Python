#Salida de consola 
nombre = 'Carlos'
edad = 26
print ("Hola tu nombre es ", nombre ,"La edad que tienes es: ", edad)
print ("Hola tu nombre es {0} y tu edad es {1:10.3f} adios {0}".format(nombre, edad)) 
# Se le da un formato {0} es la variable que se encuenta al inicio(nombre), 10.3 son 10 espacios a la izq y 3 decimales despues del punto f = flotante
print(f"Tu nombre es {nombre} edad {edad: 10.3f}")# f format es para dar formato a las variables