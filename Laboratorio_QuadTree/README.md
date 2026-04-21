# Laboratorio: QuadTree

## Descripción
Este proyecto implementa un árbol **QuadTree** desde cero para resolver problemas de búsqueda espacial en un conjunto de puntos en un plano cartesiano.  

Se comparan dos enfoques:

- QuadTree  
- Fuerza bruta  

---

## Funcionalidades

### Construcción del QuadTree
Se construye un árbol que divide el espacio en cuatro regiones (cuadrantes) de forma recursiva.  

Cada nodo representa un área rectangular definida por:
- Un punto central (x, y)
- Un ancho (w)
- Un alto (h)

Cuando un nodo supera su capacidad (en este caso 1 punto por nodo), se subdivide en cuatro hijos y redistribuye sus puntos. Este proceso continúa hasta cumplir las condiciones de parada.

---

### Cálculo de distancia
La distancia entre dos puntos se calcula en metros usando distancia euclidiana:

**distancia = sqrt((x1 - x2)^2 + (y1 - y2)^2)**

---

### Vecino más cercano (Nearest Neighbor)
Dado un punto de consulta, el algoritmo encuentra el punto más cercano utilizando el QuadTree.

Se utiliza **poda**, lo que significa que:
- Si una región no puede contener un punto más cercano que el mejor encontrado, se descarta completamente.
- Esto reduce significativamente el número de comparaciones.

También se implementa una versión de **fuerza bruta** para comparación.

---

### Búsqueda por radio (Range Search)
Permite encontrar todos los puntos dentro de un radio dado.

El QuadTree optimiza la búsqueda:
- Solo recorre nodos que intersectan con el círculo de búsqueda.
- Evita evaluar regiones completas innecesarias.

También se compara con fuerza bruta.

---

### Generación de datos
Se generan puntos aleatorios en un plano cartesiano:

- Rango típico: entre -5000 y 5000 metros
- Simula ubicaciones distribuidas en una zona

---

## Pruebas

Se incluyen pruebas básicas para validar el funcionamiento:

- Ejecución general con datos aleatorios  
- Verificación de punto exacto  
- Estabilidad del algoritmo de vecino más cercano  

---

## Visualización

Se generan gráficos que muestran:

- Distribución de puntos  
- Punto de consulta  
- Puntos dentro del radio  
- Vista general y zoom  

---

## Comparación de rendimiento

Se mide el tiempo de ejecución para:

- Vecino más cercano  
- Búsqueda por radio  

Comparando:

- QuadTree  
- Fuerza bruta  

---

## Gráficas de resultados

Se generan gráficas para analizar:

- Cómo cambia el tiempo con el número de puntos  
- Cómo afecta el radio al rendimiento  

---

## Unidades de medida

Todos los cálculos se realizan en metros:

- Coordenadas (x, y)  
- Tamaño de nodos  
- Distancias  
- Radio de búsqueda  

Esto hace que la implementación sea más simple y consistente.

---

## Conclusiones

El QuadTree es eficiente para:

- Búsquedas locales  
- Consultas de vecino más cercano  

Mantiene tiempos de consulta bajos incluso con grandes volúmenes de datos gracias a la poda espacial.

Sin embargo:

- El costo de construcción puede ser alto debido a muchas subdivisiones  
- En búsquedas por radio grandes, su rendimiento disminuye  
- Cuando el radio cubre gran parte del espacio, la fuerza bruta puede igualar o superar su rendimiento  

---

## Ejecución en Google Colab

1. Abrir Google Colab  
2. Copiar y pegar el código celda por celda o exportar el notebook directamente 
3. Ejecutar celda por celda en orden  

El código generará:

- Resultados en consola  
- Visualizaciones  
- Gráficas de rendimiento  

---

## Nota

Este proyecto es una implementación académica en la cual se busca:

- Entender el funcionamiento del QuadTree (con capacidad 1 por nodo)
- Analizar su rendimiento  
 
