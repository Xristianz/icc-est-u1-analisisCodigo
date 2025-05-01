class MetodosOrdenamiento:
    def sortByBubble(self,arreglo):
        arreglo=arreglo.copy()
        n=len(arreglo)
        for i in range (n):
            for j in range (i+1, n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i],arreglo[j]=arreglo[j],arreglo[i]
        return arreglo
    def sortBySeleccion(self,arreglo):
        n=len(arreglo)
        for i in range(n):
            min=i
            for j in range(i+1,n):
                if arreglo[j]<arreglo[min]:
                    smallerNumber = arreglo[min]
                    arreglo[min] = arreglo[i]
                    arreglo[i] = smallerNumber
            return arreglo    