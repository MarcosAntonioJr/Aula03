#Crie um algoritmo para ler um arquivo texto.

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

print(ler_arquivo('arquivo.txt'))

