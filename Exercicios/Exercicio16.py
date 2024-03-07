#Crie um algoritmo para consolidar um ou mais arquivos de texto de um diretório.

import os

def consolidar_arquivos(diretorio):
    arquivos = os.listdir(diretorio)
    conteudo = ''
    for arquivo in arquivos:
        with open(diretorio + '/' + arquivo, 'r') as a:
            conteudo += a.read() + '\n'
    return conteudo

print(consolidar_arquivos('arquivos'))
