#Crie um algoritmo para ler dados de um CSV (que possui os meses e valores de vendas), retornando qual o mês teve mais vendas.

import csv

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        vendas = {}
        for linha in leitor:
            vendas[linha[0]] = int(linha[1])
        return max(vendas, key=vendas.get)

print(ler_arquivo_csv('arquivo.csv'))

