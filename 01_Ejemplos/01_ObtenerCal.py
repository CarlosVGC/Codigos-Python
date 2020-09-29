# Programa que obtiene calificacion de un alumno
'''
practicas 40%
participacion 20%
examen 40%
'''

pract = float(input("Ingrese la calificacion de las practicas: "))
part = float(input("Ingrese la calificacion de las participacion: "))
exam = float(input("Ingrese la calificacion de las examen: "))

cal = (pract*.40)+(part*.20)+(exam*.40)

print(f"La calificacion del alumno es: {cal:.2f}")