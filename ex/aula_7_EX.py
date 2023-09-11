"""
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre
o valor da mesma

Crie uma função que fala se um número é par
ou ímpar.
"""

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    total_par = 'Par' if (total%2 == 0) else 'Ímpar'
    return f'A multiplicação teve resultado {total},\nO número {total} é {total_par}'

print(multiplicacao(3, 3, 3, 3))