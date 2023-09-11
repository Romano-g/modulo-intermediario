# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']


def zipper(a, b):
    return f'({a}, {b})'


lista3 = []


for i, local in enumerate(lista1):
    a = lista1[i]
    b = lista2[i]
    res = zipper(a, b)
    lista3.append(res)


print(lista3)  # PORRA CARALHO CONSEGUI


# Solução prof:

def zipper2(lista1, lista2):
    return [
        (lista1[i], lista2[i]) for i in range(min(len(lista1), len(lista2)))
    ]


print(zipper2(lista1, lista2))
