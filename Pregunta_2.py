"""Ejercicio de lista"""
"""Crear un programa que contenga 20 número aleatorios"""
"""Mostrar en pantalla su cuadrado y su cubo"""

import random
listaNumeros = []

for indice in range(1, 21):
    listaNumeros.append(random.randint(1, 20))

print(listaNumeros)

"""Contar los valores de mi lista"""
print(len(listaNumeros))

"""Segundo recorrido"""

for numero in listaNumeros:
    print("Número: ", numero, ", Cuadrado: ", numero**2, ", Cubo: ", numero**3)