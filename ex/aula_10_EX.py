"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebido
"""
numero = input('Digite um número: ')

def multiplos(multiplo):
    def vezes(numero):
        return multiplo * numero
    return vezes
    
duplo = multiplos(2)
triplo = multiplos(3)
quadruplo = multiplos(4)

try:
    print(f'O dobro de {numero} é: {duplo(int(numero))}')
    print(f'O triplo de {numero} é: {triplo(int(numero))}')
    print(f'O quádruplo de {numero} é: {quadruplo(int(numero))}')

except:
    print('Você não digitou um número!')