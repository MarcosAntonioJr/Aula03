#Implemente um algoritmo para encontrar a menor string em uma lista de strings.

def menor_string(lista):
    menor = lista[0]
    for i in lista:
        if len(i) < len(menor):
            menor = i
    return menor

print(menor_string(['a', 'ab', 'abc', 'abcd', 'abcde']))




