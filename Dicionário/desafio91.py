from random import randint
from time import sleep
from operator import itemgetter
while True:
    dado = {
        'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)
    }
    raking = []
    print('Valores sorteados : ')
    for k,v in dado.items():
        print(f'O {k} tirou : {v}')
        sleep(1)
    raking = sorted(dado.items(), key=itemgetter(1), reverse=True)
    print('-='*30)
    print(' ==RAKING DOS JOGADORES== ')
    for i,v in enumerate(raking):
        print(f' {i+1}º lugar : {v[0]} com {v[1]}')
        sleep(1)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] : ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print('FIM DE JOGO !')