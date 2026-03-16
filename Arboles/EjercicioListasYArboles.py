import random
import time

# Función para la genración aleatoria de estudiantes
# ------------------------------------
# GENERACIÓN ALEATORIA DE ESTUDIANTES
# ------------------------------------
def generar_estudiantes(n=10000):
    nombres = [
        "Ana", "Carlos", "Maria", "Juan", "Pedro", "Luisa", "Sofia",
        "Andres", "Camila", "David", "Laura", "Mateo", "Valentina",
        "Daniel", "Sara", "Miguel", "Paula", "Sebastian", "Elena"
    ]

    estudiantes = []
    ids = random.sample(range(1000, 100000), n)  # IDs únicos

    for i in range(n):
        estudiante = {
            "id": ids[i],
            "nombre": random.choice(nombres),
            "promedio": round(random.uniform(0, 10), 2)
        }
        estudiantes.append(estudiante)

    return estudiantes

# Función para meter los estudiantes a una lista
# -----------------------------
# LISTA
# -----------------------------
def lista_llegada(estudiantes):
    lista = []

    for estudiante in estudiantes:
        lista.append(estudiante)

    return lista

# Código Árbol ABB
# -----------------------------
# ÁRBOL ABB
# -----------------------------
class NodoABB:

    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None

class ArbolABB:
    
    def __init__(self):
        self.raiz = None

    def insertar(self, estudiante):
        if self.raiz is None:
            self.raiz = NodoABB(estudiante)
        else:
            self._insertar_rec(self.raiz, estudiante)

    def _insertar_rec(self, nodo, estudiante):
        
        if estudiante["id"] < nodo.estudiante["id"]:
            if nodo.izquierda is None:
                nodo.izquierda = NodoABB(estudiante)
            else:
                self._insertar_rec(nodo.izquierda, estudiante)

        else:
            if nodo.derecha is None:
                nodo.derecha = NodoABB(estudiante)
            else:
                self._insertar_rec(nodo.derecha, estudiante)

    def buscar(self, id_buscar):
        return self._buscar_rec(self.raiz, id_buscar)

    def _buscar_rec(self, nodo, id_buscar):

        if nodo is None:
            return None

        if nodo.estudiante["id"] == id_buscar:
            return nodo.estudiante

        if id_buscar < nodo.estudiante["id"]:
            return self._buscar_rec(nodo.izquierda, id_buscar)
        else:
            return self._buscar_rec(nodo.derecha, id_buscar)

# Código Árbol B+
# -----------------------------
# ÁRBOL B+
# -----------------------------
class NodoBPlus:
    def __init__(self, hoja=False):
        self.hoja = hoja
        self.claves = []
        self.hijos = []
        self.siguiente = None  # conecta hojas

class ArbolBPlus:

    def __init__(self, orden=3):
        self.raiz = NodoBPlus(True)
        self.orden = orden

    def insertar(self, clave, valor):
        raiz = self.raiz

        if len(raiz.claves) == (2 * self.orden) - 1:
            nueva_raiz = NodoBPlus()
            nueva_raiz.hijos.append(raiz)

            self._dividir_hijo(nueva_raiz, 0)
            self._insertar_no_lleno(nueva_raiz, clave, valor)

            self.raiz = nueva_raiz
        else:
            self._insertar_no_lleno(raiz, clave, valor)

    def _insertar_no_lleno(self, nodo, clave, valor):

        if nodo.hoja:
            i = len(nodo.claves) - 1
            nodo.claves.append((None, None))

            while i >= 0 and clave < nodo.claves[i][0]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1

            nodo.claves[i + 1] = (clave, valor)

        else:
            i = len(nodo.claves) - 1

            while i >= 0 and clave < nodo.claves[i][0]:
                i -= 1

            i += 1

            if len(nodo.hijos[i].claves) == (2 * self.orden) - 1:
                self._dividir_hijo(nodo, i)

                if clave > nodo.claves[i][0]:
                    i += 1

            self._insertar_no_lleno(nodo.hijos[i], clave, valor)

    def _dividir_hijo(self, padre, i):

        orden = self.orden
        nodo = padre.hijos[i]
        nuevo = NodoBPlus(nodo.hoja)

        padre.hijos.insert(i + 1, nuevo)
        padre.claves.insert(i, nodo.claves[orden - 1])

        nuevo.claves = nodo.claves[orden:(2 * orden) - 1]
        nodo.claves = nodo.claves[0:orden - 1]

        if not nodo.hoja:
            nuevo.hijos = nodo.hijos[orden:(2 * orden)]
            nodo.hijos = nodo.hijos[0:orden]

    def buscar(self, clave, nodo=None):

        if nodo is None:
            nodo = self.raiz

        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i][0]:
            i += 1

        if nodo.hoja:
            if i < len(nodo.claves) and nodo.claves[i][0] == clave:
                return nodo.claves[i][1]
            return None

        return self.buscar(clave, nodo.hijos[i])
    
#Código para medir los tiempos de búsqueda

# -----------------------------
# BUSQUEDA EN LISTAS
# -----------------------------
def buscar_lista(lista, id_buscar):
    for estudiante in lista:
        if estudiante["id"] == id_buscar:
            return estudiante
    return None

def buscar_lista_ordenada(lista, id_buscar):

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if lista[medio]["id"] == id_buscar:
            return lista[medio]

        elif lista[medio]["id"] < id_buscar:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return None

# -----------------------------
# MEDIR TIEMPO DE BUSQUEDA
# -----------------------------
def medir_tiempos(lista, lista_ordenada, abb, bplus, estudiantes, num_busquedas, modo="aleatorio"):

    ids = [e["id"] for e in estudiantes]

    if modo == "aleatorio":
        ids_busqueda = random.choices(ids, k=num_busquedas)

    elif modo == "ordenado":
        ids_busqueda = sorted(ids[:num_busquedas])

    # LISTA NORMAL
    inicio = time.perf_counter()
    for i in ids_busqueda:
        buscar_lista(lista, i)
    t_lista = time.perf_counter() - inicio


    # LISTA ORDENADA
    inicio = time.perf_counter()
    for i in ids_busqueda:
        buscar_lista_ordenada(lista_ordenada, i)
    t_lista_ord = time.perf_counter() - inicio


    # ABB
    inicio = time.perf_counter()
    for i in ids_busqueda:
        abb.buscar(i)
    t_abb = time.perf_counter() - inicio


    # B+
    inicio = time.perf_counter()
    for i in ids_busqueda:
        bplus.buscar(i)
    t_bplus = time.perf_counter() - inicio


    return t_lista, t_lista_ord, t_abb, t_bplus

# -----------------------------
# PROGRAMA PARA COMPARACIÓN
# -----------------------------
def comparar_tiempos():

    estudiantes = generar_estudiantes(10000)

    lista = estudiantes.copy()
    lista_ordenada = sorted(estudiantes, key=lambda x: x["id"])

    # ABB
    abb = ArbolABB()
    for e in estudiantes:
        abb.insertar(e)

    # B+
    bplus = ArbolBPlus(3)
    for e in estudiantes:
        bplus.insertar(e["id"], e)

    pruebas = [100, 1000, 2000, 4000]

    print("\n===== BUSQUEDA ALEATORIA =====")

    for p in pruebas:

        t_lista, t_lista_ord, t_abb, t_bplus = medir_tiempos(
            lista, lista_ordenada, abb, bplus, estudiantes, p, "aleatorio"
        )

        print(f"\nBusquedas: {p}")
        print(f"Lista:           {t_lista:.6f} s")
        print(f"Lista Ordenada:  {t_lista_ord:.6f} s")
        print(f"ABB:             {t_abb:.6f} s")
        print(f"B+:              {t_bplus:.6f} s")


    print("\n===== BUSQUEDA ORDENADA =====")

    for p in pruebas:

        t_lista, t_lista_ord, t_abb, t_bplus = medir_tiempos(
            lista, lista_ordenada, abb, bplus, estudiantes, p, "ordenado"
        )

        print(f"\nBusquedas: {p}")
        print(f"Lista:           {t_lista:.6f} s")
        print(f"Lista Ordenada:  {t_lista_ord:.6f} s")
        print(f"ABB:             {t_abb:.6f} s")
        print(f"B+:              {t_bplus:.6f} s")


# -----------------------------
# EJECUTAR
# -----------------------------
comparar_tiempos()