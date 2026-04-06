# 🧪 Laboratorio: Hash SHA-256 y Árbol de Merkle

## 📌 Descripción

Este trabajo aborda dos problemas relacionados con criptografía:

1. Encontrar una secuencia de números que genere un hash SHA-256 dado.
2. Determinar el orden correcto de transacciones que produce un Merkle Root específico.

Ambos problemas ilustran propiedades fundamentales como la **no reversibilidad de funciones hash** y la **dependencia del orden en estructuras tipo árbol de Merkle**.

---

## 🔐 Problema 1: Inversión de SHA-256

### 📖 Enunciado

Dado un hash SHA-256, encontrar la secuencia de 10 dígitos (cada uno entre 0 y 9) que lo genera.

---

### ⚙️ Funcionamiento

El algoritmo:

1. Genera todas las combinaciones posibles de 10 dígitos.
2. Calcula el hash SHA-256 de cada combinación.
3. Compara el resultado con el hash objetivo.
4. Si coincide, devuelve la secuencia encontrada.

---

### ⚠️ Consideraciones

* SHA-256 es una función **no reversible**.
* La forma de encontrar la entrada es mediante **fuerza bruta**.
* El espacio de búsqueda es:

[
10^{10} = 10,000,000,000 \text{ combinaciones}
]

---

## 🌳 Problema 2: Árbol de Merkle

### 📖 Enunciado

Dado un conjunto de transacciones y un Merkle Root, determinar el orden correcto de las transacciones.

---

### ⚙️ Funcionamiento

#### 1. Hash de transacciones

Cada transacción se convierte en su hash SHA-256.

#### 2. Construcción del árbol

* Los hashes se agrupan de dos en dos.
* Se concatenan y se vuelve a aplicar SHA-256.
* Este proceso se repite hasta obtener un único hash: el **Merkle Root**.

#### 3. Caso impar

Si hay un número impar de hashes:

* El último hash se **sube de nivel**
* Luego se procesa normalmente

---

### 🔁 Búsqueda del orden correcto

El algoritmo:

1. Genera todas las permutaciones posibles de las transacciones.
2. Calcula el Merkle Root para cada orden.
3. Compara con el root objetivo.
4. Retorna el orden que coincide.

---

### ⚠️ Complejidad

El número de combinaciones es:

[
n!
]

Ejemplo:

* 3 transacciones → 6 combinaciones
* 5 transacciones → 120 combinaciones

---

### 🧠 Importancia del orden

El Merkle Root depende directamente del orden de las transacciones.
Cambiar el orden produce un hash completamente distinto.

---

## 🧪 Validación

Para verificar el funcionamiento:

* Se utilizan casos pequeños (ej: 3 transacciones)
* Se calcula un root conocido
* Se comprueba que el algoritmo lo encuentra correctamente

---

## 🚀 Conclusiones

* Las funciones hash como SHA-256 son seguras debido a su naturaleza unidireccional.
* Los árboles de Merkle permiten verificar integridad de datos de forma eficiente.
* Ambos problemas requieren búsqueda exhaustiva debido a la ausencia de métodos directos de inversión.

---

## 🛠️ Tecnologías utilizadas

* Python
* Librería `hashlib`
* Librería `itertools`

---

## 📌 Nota final

Estos conceptos son fundamentales en sistemas como blockchain, donde la integridad y el orden de los datos son críticos.

Código y Readme proporcionado por IA
