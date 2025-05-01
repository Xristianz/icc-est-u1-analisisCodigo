import random
import time
from Metodos_ordenamiento import MetodosOrdenamiento
class Benchmarking:
    def __init__(self):
        print('bench inicializado')
        arreglo= self.build_arreglo(1000)
        self.mOrdenamiento=MetodosOrdenamiento()
        tarea=lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis=self.contar_con_current_time_milles(tarea)
        tiempoNano=self.contar_con_nano_time(tarea)
        print(f'Tiempo en mili {tiempoMillis}')
        print(f'tiempo en nano {tiempoNano}')

    def ejemplo(self):
        self.mO=MetodosOrdenamiento()
    def build_arreglo(self,size):
        array=[]
        for i in range (size):
            numero= random.randint(0,99999)
            array.append(numero)
        return array
        
    def contar_con_current_time_milles(self, tarea):
        inicio=time.time()
        tarea()
        fin=time.time()
        tarea()
        return fin-inicio

    def contar_con_nano_time(self,tarea):
        inicio=time.time_ns()
        tarea()
        fin=time.time_ns()
        tarea()
        return (fin-inicio)/1000000000
    def medir_tiempo(self,tarea,array):
        inicio=time.perf_counter()
        tarea(array)
        fin=time.perf_counter()
        return fin-inicio
        
        

