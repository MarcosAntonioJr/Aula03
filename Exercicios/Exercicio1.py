#Crie uma função que conte o número de vogais em uma string.

def contar_vogais(palavra):
    vogais = 'aeiou'
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais('banana'))
