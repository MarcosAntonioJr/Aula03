#Crie uma função que encontre os k maiores elementos em uma lista, mantendo a ordem original.

def k_maior(lista, k):
    lista.sort()
    return lista[-k:]

print(k_maior([1, 2, 3, 4, 5], 3))

