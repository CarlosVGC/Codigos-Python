'''
import pandas as pd

file = pd.read_csv(‘filepath’)
print(file.head()) #or file.shape() to get the number of rows and columns
file['New Column'] = #NaN or NULL
file.shape() #now check you have successfully added new column
'''
#Este código funciona para agregar filas
'''
import csv
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
''' 


def columnan():
    archivo = pd.read_csv("innovators.csv")
    ver = ['q','e','t','w']
    verp = [9,10,11,12]
    
    print(archivo.head())
    archivo['ver'] = ver 
    archivo['verp'] = verp
    archivo.head()
    archivo.to_csv('innovators.csv',encoding = 'utf8',index=False)
    
    archivo = pd.read_csv("innovators.csv")
    ver = ['q','e','t','w']
    verp = [9,10,11,12]
    
    print(archivo.head())
    archivo['ver'] = ver 
    archivo['verp'] = verp
    archivo.head()
    archivo.to_csv('innovators.csv',encoding = 'utf8',index=False)
    '''
    Info_ver = pd.DataFrame({'Verduras': ver,
                                      'Verdura Precio': verp
                                    })
    
    Info_ver.to_csv('innovators.csv', encoding = 'utf8')
    '''

def columna7():
    archivo = pd.read_csv("innovators.csv")
    fruta = ['o','p','q','r']
    frutap = [100,105,110,120]
    
    print(archivo.head())
    archivo['fruta'] = fruta 
    archivo['frutap'] = frutap
    archivo.head()
    archivo.to_csv('innovators.csv',encoding = 'utf8',index=False)
    
    
import pandas as pd
#codigo crea archivo cvs vacio 
df = pd.DataFrame(list())
df.to_csv('innovators.csv', encoding = 'utf8')
df.to_csv('info1.csv', encoding = 'utf8')
df.to_csv('info2.csv', encoding = 'utf8')
df.to_csv('info3.csv', encoding = 'utf8')

nombre = ['a','b','c','d']
precio = [5,6,7,8]

nombre2 = ['e','f','g','h']
precio2 = [9,10,11,12]

lata = ['e','f','g','h']
latap = [9,10,11,12]


df = pd.read_csv("innovators.csv")

df ['nombre'] = nombre
df.to_csv('innovators.csv')
df ['precio'] = precio
df.to_csv('innovators.csv')

df ['nombre2'] = nombre2
df.to_csv('innovators.csv')
df ['precio2'] = precio2
df.to_csv('innovators.csv')

Info_enlatados = pd.DataFrame({'Enlatados': lata,
                                      'Precio': latap
                                    })
    
Info_enlatados.to_csv('innovators.csv', encoding = 'utf8',index=False)

#df.to_csv('innovators.csv')

columnan()
columna7()
        

'''
df = pandas.read_csv("____.csv")

define the data you want to add

color=[‘red’ , ’blue’ , ’green’]

create new column name ‘color’

df ['color'] = color

for checking the new column

print(df)

convert it back to csv file

df.to_csv('_____.csv')
'''