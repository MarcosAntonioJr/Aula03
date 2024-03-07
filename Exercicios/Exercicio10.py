#.Criar um algoritmo para calcular a frequência que uma palavra aparece em um texto.

def contar_ocorrencias(frase, palavra):
    return frase.count(palavra)

print(contar_ocorrencias('Pedro parecia estranho, ele não falou com ninguém na aula. Nesse exemplo, percebe-se que a anáfora ocorre na relação entre “Pedro” e o pronome “ele”. Na primeira oração, o referente aparece de modo direto “Pedro”, permitindo ao leitor/ouvinte saber qual é o tema da frase.', 'Pedro'))

