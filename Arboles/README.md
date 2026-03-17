# Este ejercicio fue hecho con ChatGPT


Comparativa de Estructuras de Datos y Algoritmos de Busqueda
Este proyecto es una herramienta de prueba para comparar que tan rapido diferentes estructuras de datos pueden encontrar informacion en un listado de 10,000 estudiantes.

## 1. ¿Que hace este codigo?
El programa genera una base de datos ficticia de 10,000 alumnos con ID, nombre y promedio. Luego, realiza miles de busquedas aleatorias usando cuatro metodos distintos para medir cual es el mas eficiente en tiempo real.

## 2. Metodos de Busqueda Explicados
Busqueda Lineal (Lista Normal)
Es el metodo mas basico. El programa revisa la lista posicion por posicion, desde el primero hasta el ultimo, hasta encontrar el ID correcto.

Problema: Si tienes millones de datos y el que buscas es el ultimo, el programa tardara mucho tiempo.

### Busqueda Binaria (Lista Ordenada)
Para que funcione, la lista debe estar ordenada por ID. El programa mira el dato central; si el ID buscado es menor, descarta la mitad derecha y busca en la izquierda. Repite esto hasta encontrarlo.

Ventaja: Es extremadamente rapido comparado con la busqueda lineal.

### Arbol Binario de Busqueda (ABB)
Es una estructura jerarquica. Cada "nodo" tiene un estudiante y dos ramas (hijos). Los IDs menores van a la izquierda y los mayores a la derecha.

Concepto clave: Utiliza "recursividad" (una funcion que se llama a si misma) para navegar por las ramas sin tener que mirar todos los datos.

### Arbol B+ (Nivel Avanzado)
Es la estructura que usan las bases de datos profesionales. A diferencia del ABB, el Arbol B+ se mantiene "balanceado".

¿Que significa balanceado?: Que el arbol se reorganiza solo (usando una funcion de division de nodos) para que todas las rutas de busqueda tengan la misma longitud. Esto garantiza que nunca se vuelva lento, sin importar cuantos datos agregues.

## 3. Como interpretar los resultados
Al correr el script, veras una comparativa de tiempos en segundos:

La Lista Normal siempre sera la mas lenta (especialmente al hacer 4,000 busquedas).

La Lista Ordenada y los Arboles (ABB y B+) mostraran tiempos muy cercanos a cero, demostrando que son estructuras optimizadas para velocidad.

## 4. Requisitos y Ejecucion
Requiere Python 3.x.

No requiere librerias externas.

Solo debes ejecutar el archivo .py y los resultados apareceran en la consola.
