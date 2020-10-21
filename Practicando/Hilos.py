#Ejemplo de uso de hilos

import threading
import time
import sumas as su

def hola():
    for a in range(100):
        print(f'hilo 1 a:{a}\n')
        time.sleep(1)
        
    
    
def hola2(nombre):
    
    for b in range(100):
        print(f'hilo 2 b:{b} te llamas {nombre}\n')
        time.sleep(1)
    
    
    
if __name__=='__main__':
    '''
    thread = threading.Thread(target = hola) #Inicializar un hilo llamando a una funcion
    thread.start()

    thread2 = threading.Thread(target=hola2, args=('Carlos',))
    thread2.start()
    '''
    
    thread3 = threading.Thread(target = su.suma) #Inicializar un hilo llamando a una funcion
    thread3.start()
    
    thread4 = threading.Thread(target = su.resta) #Inicializar un hilo llamando a una funcion
    thread4.start()
    
    thread5 = threading.Thread(target = su.mul) #Inicializar un hilo llamando a una funcion
    thread5.start()