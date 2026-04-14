# Laboratorio: KD-Tree

## Descripción

Este proyecto implementa un árbol KD (KD-Tree) desde cero para resolver problemas de búsqueda espacial en un conjunto de puntos geográficos. Se trabaja con coordenadas (latitud, longitud) simuladas y se comparan dos enfoques:

* KD-Tree
* Fuerza bruta



## Funcionalidades

### Construcción del KD-Tree

Se construye un árbol binario donde en cada nivel se divide el espacio alternando entre dimensiones (latitud y longitud). Esto permite organizar los datos de forma eficiente para consultas espaciales.


### Cálculo de distancia

Se calcula la distancia entre dos puntos en metros usando una aproximación basada en latitud y longitud.


### Vecino más cercano (Nearest Neighbor)

Dado un punto de consulta, el algoritmo encuentra el punto más cercano utilizando el KD-Tree. También se implementa una versión de fuerza bruta para comparación.


### Búsqueda por radio (Range Search)

Permite encontrar todos los puntos dentro de un radio dado desde una ubicación. El KD-Tree utiliza poda espacial para evitar recorrer todos los puntos.


### Generación de datos

Se generan puntos aleatorios alrededor de una ubicación base para simular direcciones en una ciudad.


### Pruebas

Se incluyen pruebas básicas para validar el funcionamiento:

* Ejecución general con datos aleatorios
* Verificación de punto exacto
* Estabilidad del algoritmo de vecino más cercano


### Visualización

Se generan gráficos que muestran:

* Distribución de puntos
* Punto de consulta
* Puntos dentro del radio
* Vista general y zoom


### Comparación de rendimiento

Se mide el tiempo de ejecución para:

* Vecino más cercano
* Búsqueda por radio

Comparando KD-Tree y fuerza bruta.


### Gráficas de resultados

Se generan gráficas para analizar:

* Cómo cambia el tiempo con el número de puntos
* Cómo afecta el radio al rendimiento


## Conclusiones

El KD-Tree es más eficiente para encontrar el vecino más cercano y para búsquedas en radios pequeños, donde puede descartar grandes regiones del espacio. Sin embargo, cuando el radio es grande, el algoritmo pierde eficiencia y su comportamiento se acerca al de fuerza bruta.


## Ejecución en Google Colab

1. Abrir Google Colab
2. Subir el notebook con el código
3. Ejecutar celda x celda en orden


El código generará:

* Resultados en consola
* Visualizaciones
* Gráficas de rendimiento


## Nota

Este proyecto es una implementación académica cuyo objetivo es entender el funcionamiento del KD-Tree y analizar su rendimiento en comparación con métodos simples.
