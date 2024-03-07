#Crie uma função que embaralhe os elementos de uma lista de forma aleatória.

import random

def embaralhar(lista):
    return random.sample(lista, len(lista))

print(embaralhar([1, 2, 3, 4, 5]))
