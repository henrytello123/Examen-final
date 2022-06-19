import random

miLista = []

for i in range(10):
    miLista.append(random.randrange(1, 20))

resultaList = []

for elemento in miLista:
    if elemento not in resultaList:
        resultaList.append(elemento)

print("La primera del item 2 sin duplicados es:", resultaList)

"""Ordenando nuestra lista de mayor a menor"""

resultaList.sort()

for numero in resultaList:
    print(numero, " ", end="")



