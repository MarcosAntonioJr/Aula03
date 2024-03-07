#Escreva um programa que substitua todas as ocorrências de uma letra em uma string por outra letra.

def substituir_letra(palavra, letra1, letra2):
    nova_palavra = ''
    for letra in palavra:
        if letra == letra1:
            nova_palavra += letra2
        else:
            nova_palavra += letra
    return nova_palavra

print(substituir_letra('banana', 'a', 'o'))