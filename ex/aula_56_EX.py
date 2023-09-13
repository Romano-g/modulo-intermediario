# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json
opcoes = [
    'listar',
    'desfazer',
    'refazer',
]


def additem(item, lista=[]):

    lista.append(item)
    return lista


lista = []
removidos = []

while True:
    resposta = input(
        'Comandos: listar, desfazer, refazer \nDigite um comando: ')

    if resposta == 'sair':
        break

    elif resposta not in opcoes:
        print()
        print(additem(resposta, lista))
        print()

    elif resposta == opcoes[0]:
        print()
        print(lista)
        print()

    elif resposta == opcoes[1]:
        try:
            item = lista.pop()
            removidos.append(item)
            print()
            print(lista)
            print()

        except:
            print()
            print('Não há o que desfazer')
            print()
            continue

    elif resposta == opcoes[2]:
        try:
            print()
            print(additem(removidos[-1], lista))
            removidos.pop()
            print()

        except:
            print()
            print('Não há nada para refazer')
            print()
            continue

    with open('aula_56_EX.json', 'w', encoding='utf8') as arquivo:
        json.dump(
            lista,
            arquivo,
            indent=2,
        )
