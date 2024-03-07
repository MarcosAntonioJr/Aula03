#Escreva um programa que encontre o par de elementos em uma lista cuja soma seja igual a um determinado valor.

import random

def encontrar_par(lista, valor):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == valor:
                return (lista[i], lista[j])
    return None

print(encontrar_par([1, 2, 3, 4, 5], 9))