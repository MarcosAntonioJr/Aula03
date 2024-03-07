#Escreva um programa que implemente a soma de matrizes usando listas aninhadas.

def soma_matrizes(matriz1, matriz2):
    matriz_soma = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[i])):
            linha.append(matriz1[i][j] + matriz2[i][j])
        matriz_soma.append(linha)
    return matriz_soma

print(soma_matrizes([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
