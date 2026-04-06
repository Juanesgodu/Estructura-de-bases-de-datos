# Se deben probar todas las combinaciones posibles hasta encontrar el orden que es con el cual se comprueba el root
# Se termina volviendo imposible en la practica si hay muchas transaciones

import hashlib
from itertools import permutations

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

def merkle(txs):
    hs = [h(x) for x in txs]
    while len(hs) > 1:
        hs = [h(hs[i] + hs[i+1]) if i+1 < len(hs) else hs[i] 
              for i in range(0, len(hs), 2)]
    return hs[0]

# Lista de Transacciones
txs = ["tx1", "tx2", "tx3"]

""" Orden que seguiria el arbol (para ilustar):

            Nivel 0 (hojas):
            h(tx1)   h(tx2)   h(tx3)

            Nivel 1:
            h(h(tx1)+h(tx2))   h(h(tx3))

            Nivel 2 (root):
            h( resultado1 + resultado2 )"""

# Root Objetivo
root_objetivo = "b7d842c653948dfc2fd7274b7d20c213c2e5311eb1fd93d69d36efd023324b61"

for p in permutations(txs):
    if merkle(list(p)) == root_objetivo:
        print("Esta es la lista para generar el orden",p)
        break
