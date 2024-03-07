#Escreva um programa que identifique todos os números primos em uma lista de números inteiros.

def num_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos(lista):
    return [x for x in lista if num_primo(x)]

print(primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
