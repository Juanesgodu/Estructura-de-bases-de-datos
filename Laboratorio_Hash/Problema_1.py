# Se tiene que hacer con fuerza bruta porque no hay forma de invertir el hash como tal
# Ademas al probar los hash en orden si es justo la ultima opción se va a demorar demasiado
# Y en casos con más opciones se termina volviendo imposible

import hashlib
from itertools import product

# Aca se pone el hash objetivo
hash_objetivo = "6e407e0e2f82994cfb808ef7c13a58adc00cc6c323837bd0ec9ed379eeba0df5"

for c in product('0123456789', repeat=10):
    s = ''.join(c)
    if hashlib.sha256(s.encode()).hexdigest() == hash_objetivo:
        print("Secuencia original:",s)
        break
