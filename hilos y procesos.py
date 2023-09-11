import threading
from threading import *
import multiprocessing
import time

def proceso_hilo(nombre):
    for i in range(5):
        print(f"{nombre}: Ejecución {i + 1}")
        time.sleep(1)

def procesamiento(nombre):
    for i in range(5):
        print(f"Proceso: Ejecución {i + 1}")
        time.sleep(1)

def hola():
  print("Hola mundo")

if __name__ == "__main__":
    # Creamos los hilos
    hilo = threading.Thread(target=proceso_hilo, args=("Hilo 1",))
    hilo2=threading.Thread(target=proceso_hilo,args=("Hilo 2",))
    hilo3 = Timer(3,hola,)  

    # Crear un proceso
    proceso = multiprocessing.Process(target=procesamiento, args=("Proceso 1",))#creamos el proceso 

    # Configuro el proceso como demonio
    proceso.daemon = True

    # Iniciamos los hilos y el proceso
    hilo.start()
    hilo2.start()
    
    proceso.start()
    hilo3.start()    

    # Esperar a que el hilo termine 
    hilo.join()
    hilo2.join()
   




   