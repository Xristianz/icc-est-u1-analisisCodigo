import java.util.Random;

public class Benchmarkin {
    private MetodosOrdenamiento metodosOrdenamiento;
    public Benchmarkin(){
        // long inicioMillis= System.currentTimeMillis();
        // long inicioNano=System.nanoTime();
        // System.out.println(tiempoMilis);
        // System.out.println(tiempoNano);
        metodosOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(100000);
        Runnable tarea = ()-> metodosOrdenamiento.burbujaTradicional(arreglo);
        double tiempoNano=medirConNanoTime(tarea);
        double tiempoMilis=medirConCurrentTime(tarea);
        System.out.println("Con mili: " + tiempoMilis);
        System.out.println("Con nano: "+ tiempoNano);
    }
    public double medirConNanoTime(Runnable tarea){
        long inicio= System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin-inicio)/1000000000.0;
        
    }
    public double medirConCurrentTime(Runnable tarea){
        long inicio=System.currentTimeMillis();
        tarea.run();
        long fin=System.currentTimeMillis();
        return(fin-inicio)/1000.0;
    }
    private int[] generarArregloAleatorio(int tamano){
        int[] arreglo = new int[tamano];
        Random random = new Random();
        for (int i=0; i<tamano;i++){
            arreglo[i]= random.nextInt(100_000);
        }
        return arreglo;
    }
        
    
}
