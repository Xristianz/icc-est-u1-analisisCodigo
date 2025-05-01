from benchmarking import Benchmarking
from Metodos_ordenamiento import MetodosOrdenamiento
if __name__ == "__main__":
    print('ejecutando')
    metodos=MetodosOrdenamiento()
    Bench = Benchmarking()
    tam=1000
    arreglo_base=Bench.build_arreglo(tam)
    metodo={
        "Borbuja":metodos.sortByBubble,
        "seleccion" :metodos.sortBySeleccion,
    }
    resultados=[]
    for nombre, metodo in metodo.items():
        tiempo=Bench.medir_tiempo(metodo,arreglo_base)
        tuplaResultado=(tam,nombre,tiempo)
        resultados.append(tuplaResultado)

    for resultado in resultados:
        tam,nombre,tiempo=resultado
        print(f"Tamano: {tam}, Metodo: {nombre} ,Tiempo: {tiempo:.6f} segundos")