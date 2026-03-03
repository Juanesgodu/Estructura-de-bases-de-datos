fil = 100000
col = 100000

matriz = []

for i in range(fil):
    fila = []
    for j in range(col):
        fila.append((i + j) & 1)
    matriz.append(fila)

with open("matriz.txt", "w") as f:
    for fila in matriz:
        for valor in fila:
            f.write(str(valor))
        f.write("\n")


# El código no funciona porque se está intentando hacer una escritura a disco de un tamaño gigantesco
# Además intenta usar la RAM en lugar de escribir directamente a disco
