#Crie um algoritmo para ler dados de um CSV (que possui o nome de vendedores e o valor de cada venda realizada), retornando qual o vendedor que mais vendeu e o que menos vendeu.

import csv

def ler_arquivo_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        vendas = {}
        for linha in leitor:
            if linha[0] not in vendas:
                vendas[linha[0]] = 0
            vendas[linha[0]] += int(linha[1])
        return max(vendas, key=vendas.get), min(vendas, key=vendas.get)

print(ler_arquivo_csv('arquivo.csv'))