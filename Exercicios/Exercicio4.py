#Crie uma função que conte o número de ocorrências de uma determinada palavra em uma frase.

def contar_ocorrencias(frase, palavra):
    return frase.count(palavra)

print(contar_ocorrencias('Quantas vezes ocorre as vezes vezes de ocorrencia', 'vezes'))
