#Crie uma função que encontre a interseção de duas listas sem usar conjuntos.

def intersecao(lista1, lista2):
    intersecao = []
    for i in lista1:
        if i in lista2:
            intersecao.append(i)
    return intersecao

print(intersecao([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))