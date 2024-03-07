#Crie um algoritmo para ler um arquivo CSV.

import csv

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

ler_arquivo_csv('arquivo.csv')
